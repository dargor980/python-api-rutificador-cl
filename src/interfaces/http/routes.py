from flask import Blueprint 
from src.infraestructure.rut_gateway import RutGateway
from src.application.rut_usecase import RutUseCase
from .controllers import PersonController


http_bp = Blueprint("http_bp", __name__)
usecase = RutUseCase(RutGateway())
controller = PersonController(usecase)

@http_bp.route("/persona/rut/<rut>", methods=["GET"])
def persona_rut(rut):
    return controller.get_person(rut)

@http_bp.route("/persona/buscar/<nombre>", methods=["GET"])
def persona_buscar(nombre):
    return controller.search_person(nombre)
