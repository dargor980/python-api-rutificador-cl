import logging 

logger = logging.getLogger("api_rutificador")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)