from exceptions.ValidationError import ValidationError


class MissingAttributeError(ValidationError):
    def __init__(self, attribute_name: str, class_name: str):
        """
        Error for missing attributes.

        :param attribute_name: Name of the missing attribut.
        :param class_name: Name of the class, in which the error was detected.
        """
        super().__init__(f"The attribut '{attribute_name}' must be set in an instance of '{class_name}'.")

