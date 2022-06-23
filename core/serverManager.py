import logging 
import uvicorn 
from fastapi import FastAPI
from api.api import api_router


LOGGER = logging.getLogger(__name__)


def create_app()-> FastAPI:
    try:
        LOGGER.info("Intializing fastapi app")
        app = FastAPI()
        app.include_router(api_router, prefix="/api/v1")
    except Exception as e:
        LOGGER.error(f"there's an error in the app initialozation {e}")
    return app

app: FastAPI = create_app()  



def run()->None :
    uvicorn.run(
        app,
        host=" 0.0.0.0",
        port= "8080",
        
    )