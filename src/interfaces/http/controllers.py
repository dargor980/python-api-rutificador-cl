from flask import jsonify, abort
from src.application.rut_usecase import RutUseCase

class PersonController:
    def __init__(self, usecase: RutUseCase):
        self.usecase = usecase
    
    def get_person(self, rut: str):
        person = self.usecase.get_person_by_rut(rut)
        if person:
            return jsonify(person.__dict__)
        abort(404)
    
    def search_person(self, name: str):
        persons = self.usecase.seach_person_by_name(name)
        return jsonify([p.__dict__ for p in persons])