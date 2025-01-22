from abc import ABC, abstractmethod

class DSLBaseClass(ABC):
    def __init__(self, **kwargs):
        all_annotations = self.get_all_annotations()
        
        for key, value in kwargs.items():
            if key in all_annotations:
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown attribute: {key}")

        self.validate()

    def get_all_annotations(self):
        annotations = {}
        for cls in self.__class__.mro():
            if hasattr(cls, '__annotations__'):
                annotations.update(cls.__annotations__)
        return annotations
    
    @abstractmethod
    def validate(self):
        pass

    def __repr__(self):
        attributes = ", ".join(
            f"{key}={getattr(self, key)}"
            for key in self.get_all_annotations()
        )
        return f"{self.__class__.__name__}({attributes})"