import pytest
from app import create_app
from src.domain.models import Person
from src.interfaces.http import routes

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_get_person_success(client, monkeypatch):
    person = Person(
        RUT="1-9",
        Nombre="Juan Perez",
        Edad="30",
        Sexo="M",
        Direccion="Calle 1",
        Ciudad="Santiago",
    )
    monkeypatch.setattr(routes.controller.usecase.gateway, "find_by_rut", lambda rut: person)
    response = client.get("/api/v1/persona/rut/1-9")
    assert response.status_code == 200
    assert response.get_json() == person.__dict__

def test_get_person_not_found(client, monkeypatch):
    monkeypatch.setattr(routes.controller.usecase.gateway, "find_by_rut", lambda rut: None)
    response = client.get("/api/v1/persona/rut/2-7")
    assert response.status_code == 404

def test_search_person(client, monkeypatch):
    persons = [
        Person(
            RUT="1-9",
            Nombre="Juan Perez",
            Edad="30",
            Sexo="M",
            Direccion="Calle 1",
            Ciudad="Santiago",
        ),
        Person(
            RUT="2-7",
            Nombre="Pedro Perez",
            Edad="25",
            Sexo="M",
            Direccion="Calle 2",
            Ciudad="Valparaiso",
        ),
    ]
    monkeypatch.setattr(routes.controller.usecase.gateway, "find_by_name", lambda name: persons)
    response = client.get("/api/v1/persona/buscar/Perez")
    assert response.status_code == 200
    assert response.get_json() == [p.__dict__ for p in persons]

