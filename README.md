# API Rutificador (Python)

Servicio HTTP construido con Flask que consulta información pública de rutificador.net usando Playwright. Permite obtener datos de una persona a partir de su RUT o buscar personas por nombre.

## Requisitos
- Python 3.10+
- Dependencias listadas en `requirements.txt`
- Navegadores de Playwright (`playwright install`)

## Variables de entorno
- `PORT`: Puerto en el que se iniciará la aplicación (por defecto 8000).
- `RUTIFICADOR_URL`: URL base del sitio a consultar (por defecto https://rutificador.net).

## Uso

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. Ejecuta el servidor:
   ```bash
   python app.py
   ```
   Por defecto escuchará en `http://localhost:8000`.

### Con Docker

También puedes construir la imagen y levantar el servicio usando Docker:

```bash
docker build -t api-rutificador .
docker run -p 8000:8000 api-rutificador
```

O bien con `docker-compose`:

```bash
docker-compose up
```

## Endpoints
- `GET /api/v1/persona/rut/<rut>`: Devuelve los datos de la persona con ese RUT.
- `GET /api/v1/persona/buscar/<nombre>`: Lista de personas cuyo nombre coincide.
