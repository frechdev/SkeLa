import re
import numpy as np
from dsl import ClassMap
import helper.ConsolePrinter as cp
from model.Component import Component
from model.ConstructionPlanSet import ConstructionPlanSet
from model.Node import Anchor
from model.Settings import Settings

class DSLInterpreter:
    
    registry = {}

    def __init__(self):
        self.constructionPlanSet = ConstructionPlanSet()


    def interpret(self, script: str):
        commands = self.parse_commands(script)
        
        for line_number, command in commands:
            try:
                self.execute_command(command, line_number)
            except Exception as e:
                cp.print_error(f"Failed interpretation of command at L. {line_number}: {e}")
                raise e
                
        return self.constructionPlanSet
                
    def parse_commands(self, script: str):
        script_lines = script.split("\n")
        commands = []
        line_number = 1

        command_buffer = ""
        for line in script_lines:
            stripped_line = line.strip()
            if not stripped_line or stripped_line.startswith("#"):
                line_number += 1
                continue

            command_buffer += stripped_line

            if stripped_line.endswith("}"):  # Kommandoende erreicht
                commands.append((line_number, command_buffer))
                command_buffer = ""
            line_number += 1

        return commands

    def execute_command(self, command: str, line_number: int):
        match = re.match(r"(\w+)\s*\{(.+)\}", command)
        if not match:
            raise ValueError(f"Invlid Command: {command}")

        class_name, attribute_str = match.groups()
        class_name = class_name.upper()

        if class_name not in ClassMap.class_map:
            raise ValueError(f"Unknown Command-Class: {class_name}")

        attributes = self.parse_attributes(attribute_str)
        cls = ClassMap.class_map[class_name]

        instance = cls(**attributes)
        print(f"Instanziiert: {instance}")

        if isinstance(instance, Settings):
            self.constructionPlanSet.settings = instance
        elif isinstance(instance, Component):
            self.constructionPlanSet.component_list.append(instance)

    def parse_attributes(self, attribute_str):
        attributes = {}

        attribute_str = attribute_str.strip()
        tokens = self.tokenize_attributes(attribute_str)

        for key, value in tokens.items():
            value = self.parse_value(value)

            attributes[key] = value

        return attributes

    def tokenize_attributes(self, attribute_str):
        tokens = {}
        current_key = None
        current_value = []
        depth = 0 

        i = 0
        while i < len(attribute_str):
            char = attribute_str[i]

            if char == ':':
                current_key = ''.join(current_value).strip()
                current_value = []
            elif char == ',' and depth == 0:
                if current_key is not None:
                    tokens[current_key] = ''.join(current_value).strip()
                    current_key = None
                current_value = []
            elif char == '[':
                depth += 1
                current_value.append(char)
            elif char == ']':
                depth -= 1
                current_value.append(char)
            elif char == '{' or char == '}':
                raise SyntaxError(f"'{char}' may not be used within the attribute list (within '{{' '}}')")
            else:
                current_value.append(char)

            i += 1

        if current_key is not None:
            tokens[current_key] = ''.join(current_value).strip()

        return tokens

    def parse_value(self, value:str):

        if value.startswith('[') and value.endswith(']'):
            list_values = value.strip()[1:-1].split(',')
            
            result = []
            for list_value in list_values:
                result.append(self.parse_value(list_value))
            
            return result


        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        if value.startswith("(") and value.endswith(")"):
            return self.parse_point(value)
        if value.startswith(">"):
            return Anchor[value[1:]]
        if value.isdigit():
            return int(value)
        
        
        return value

    def parse_point(self, point_command:str) -> np.array:
        point_str_list = point_command.split('+')
        
        point = np.zeros(2)
        for point_str in point_str_list:
            point_str = point_str.strip()

            match = re.match(r'^\(([-\d]+)\s*([-\d]+)\)$', point_str)
            if match:
                point += np.array([int(match.group(1)), int(match.group(2))])
                
            match = re.match(r'^\(([\w-]+)-([\w\d]+)\)$', point_str)
            if match:
                pnt = self.constructionPlanSet.get_coordinates_of_point(match.group(1), match.group(2))
                point += pnt
            
        return point        
        

