from exceptions.ValidationError import ValidationError
from model.DSLBaseClass import DSLBaseClass


class Settings(DSLBaseClass):
    page_size: str = "A4"
    scale_divisor: int = 100
    compass_rotation: int = 0
    version: str = "v00.00"
    
    def validate(self):
        if self.page_size not in {"A4", "A3"}:
            raise ValidationError(f"Value '{self.page_size}' is not supported for attribut 'page_size'")
        if not isinstance(self.scale_divisor, int) or self.scale_divisor < 0:
            raise ValidationError("Value for attribut 'scale_divisor' must be positive and integer.")
        
        return super().validate()