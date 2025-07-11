from typing import List 
from src.domain.models import Person
from src.domain.ports import RutGatewayPort

class RutUseCase:
    def __init__(self, gateway: RutGatewayPort):
        self.gateway = gateway

    def get_person_by_rut(self, rut: str) -> Person | None:
        return self.gateway.find_by_rut(rut)

    def seach_person_by_name(self, name: str) -> List[Person]:
        return self.gateway.find_by_name(name)