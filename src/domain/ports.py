from abc import ABC, abstractmethod
from typing import List 
from .models import Person 

class RutGatewayPort(ABC):
    @abstractmethod
    def find_by_rut(self, rut: str) -> Person | None:
        pass 

    def find_by_name(self, name: str) -> List[Person]:
        pass