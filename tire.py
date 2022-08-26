from serviceable import Serviceable
from abc import ABC

class Tire(Serviceable, ABC):
    pass

class CarriganTire(Tire):
    def __init__(self, worn_data: "list[int]") -> None:
        self.worn_data = worn_data
    
    def needs_service(self) -> bool:
        return any([d >= 0.9 for d in self.worn_data])

class OctoprimeTire(Tire):
    def __init__(self, worn_data: "list[int]") -> None:
        self.worn_data = worn_data
    
    def needs_service(self) -> bool:
        return sum(self.worn_data) >= 3
