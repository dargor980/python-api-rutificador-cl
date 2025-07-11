from flask import Blueprint 
#aca llamaria al controlador

def create_routes(app):
    blueprint = Blueprint("api", __name__)

    rut_controller = create_rut_controller()

    blueprint.add_url_rule("/api/v1/persona/rut/<rut>", "funcion", rut_controller)

    app.register_blueprint(blueprint)