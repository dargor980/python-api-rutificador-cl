import requests 
from bs4 import BeautifulSoup
from typing import List 
from src.domain.models import Person 
from src.domain.ports import RutGatewayPort
from src.config.settings import settings
from .logger import logger 
from playwright.sync_api import sync_playwright
from playwright_stealth.stealth import Stealth

class RutGateway(RutGatewayPort):
    def _fetch(self, action: str, value: str) -> BeautifulSoup:

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=100)
            context = browser.new_context()
            page = context.new_page()

            url = settings.RUTIFICADOR_URL
            if action == "search_by_rut":
                url = url + "/rut"

            page.goto(url, timeout=60000)

            selector = ""
            if action == "search_by_rut":
                selector = "input[name='rut']"
            else:
                selector = "input[name='nombre']"
            page.wait_for_selector(selector)
            page.fill(selector, value)


            page.click("button#btn-buscar")

            page.wait_for_selector("tbody tr", timeout=10000)

            html = page.content()

            browser.close()

            return BeautifulSoup(html, "html.parser")
    
    def find_by_rut(self, rut: str) -> Person | None:
        soup = self._fetch("search_by_rut", rut)
        rows = soup.select("tbody tr")
        for row in rows:
            cols = [td.text.strip() for td in row.select("td")]
            if len(cols) >= 6:
                return Person(
                    RUT=cols[0], Nombre=cols[1], Edad=cols[2],  Sexo=cols[3],
                    Direccion=cols[4], Ciudad=cols[5]
                )
        logger.debug(f"No se encontró RUT {rut}")
        return None
    
    def find_by_name(self, name: str) -> List[Person]:
        soup = self._fetch("search_by_name", name)
        persons = []
        for row in soup.select("tbody tr"):
            cols = [td.text.strip() for td in row.select("td")]
            if len(cols) >=5 :
                persons.append(
                    Person(
                        RUT=cols[0], Nombre=cols[1], Sexo=cols[2],
                        Ciudad=cols[3], Direccion=cols[4], Edad=""
                    )
                )
        return persons