import os 
from dataclasses import dataclass

@dataclass
class Settings:
    PORT: int = int(os.getenv("PORT", 8000))
    RUTIFICADOR_URL: str = "https://rutificador.net"

settings = Settings()