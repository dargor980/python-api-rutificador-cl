from flask import Flask 
from src.config.settings import settings
from src.infraestructure.logger import logger 
from src.interfaces.http.routes import http_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(http_bp, url_prefix="/api/v1")
    return app 



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=settings.PORT)
    logger.info(f"Server running on port {settings.PORT}")



