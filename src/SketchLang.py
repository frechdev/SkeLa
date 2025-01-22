import argparse
import os
import helper.ConsolePrinter as cp
from dsl.DSLInterpreter import DSLInterpreter
from model.ConstructionPlanSet import ConstructionPlanSet
from exceptions.InputError import InputError
from svgwriter.ConstructionPlanWriter import ConstructionPlanWriter


def read_dsl_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_data(skript_file):
    interpreter = DSLInterpreter(skript_file)
    return interpreter.interpret()

def main():
    parser = argparse.ArgumentParser(description="Erzeugt einen Bauplan auf Basis einer Bemaßungstabelle.")
    parser.add_argument('daten', type=str, help='Pfad der Bemaßungstabelle')
    parser.add_argument('--debug', action="store_true", help='Erweitert die Zeichnung um Informationen, die die Arbeit mit der Zeichnung erleichtern.')
    parser.add_argument('--svg', action="store_true", help='Erzeugt zusätzlich die rohen svg-Dateien.')
    
    args = parser.parse_args()
    file_path = args.daten
    debug_mode = args.debug
    is_savig_svg = args.svg
    
    file_path_without_ext, ext = os.path.splitext(file_path)

    dsl_script = read_dsl_file(file_path)

    interpreter = DSLInterpreter()
    constructionPlanSet = interpreter.interpret(dsl_script)
    
    constructionPlanWriter = ConstructionPlanWriter(file_path_without_ext, constructionPlanSet, debug_mode)
    constructionPlanWriter.write(is_savig_svg)


if __name__ == '__main__':    
    try:
        main()
    except InputError as e: cp.print_error(e)
        
        
    


