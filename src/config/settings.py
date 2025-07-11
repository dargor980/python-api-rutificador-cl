import os 
from dataclasses import dataclass

@dataclass
class Settings:
    PORT: int = int(os.getenv("PORT", 5000))
    RUTIFICADOR_URL: str = "https://rutificador.org/backend.php"

settings = Settings()