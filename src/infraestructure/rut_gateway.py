import requests 
from bs4 import BeautifulSoup
from typing import List 
from src.domain.models import Person 
from src.domain.ports import RutGatewayPort
from src.config.settings import settings
from .logger import logger 

class RutGateway(RutGatewayPort):
    def _fetch(self, action: str, value: str) -> BeautifulSoup:
        form = {"action": action}
        form["rut" if action == "search_by_rut" else "name"] = value 
        response = requests.post(settings.RUTIFICADOR_URL, data=form)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    
    def find_by_rut(self, rut: str) -> Person | None:
        soup = self._fetch("search_by_rut", rut)
        rows = soup.select("tbody tr")
        for row in rows:
            cols = [td.text.strip() for td in row.select("td")]
            if cols[1]:
                return Person(
                    RUT=cols[1], Nombre=cols[0], Sexo=cols[2],
                    Direccion=cols[3], Ciudad=cols[4]
                )
        logger.debug(f"No se encontró RUT {rut}")
        return None
    
    def find_by_name(self, name: str) -> List[Person]:
        soup = self._fetch("search_by_name", name)
        persons = []
        for row in soup.select("tbody tr"):
            cols = [td.text.strip() for td in row.select("td")]
            if cols[0]:
                persons.append(
                    Person(
                        RUT=cols[0], Nombre=cols[1], Sexo=cols[2], 
                        Direccion=cols[3], Ciudad=cols[4]
                    )
                )
        return persons