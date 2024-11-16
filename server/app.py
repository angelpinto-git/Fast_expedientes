from fastapi import FastAPI

from .api import router_api

app = FastAPI()

# Incluimos el reouter principal a la instancia de FastAPI
app.include_router(router_api)

