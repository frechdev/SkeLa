class ValidationError(Exception):
    def __init__(self, msg: str):
        """
        Error accured after validating.

        :param attribute_name: Name of the missing attribut.
        :param class_name: Name of the class, in which the error was detected.
        """
        super().__init__(f"Validation Failed: {msg}")

