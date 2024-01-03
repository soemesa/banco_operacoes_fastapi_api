import uvicorn
from fastapi import FastAPI

from src.rotas import router


def app():
    api = FastAPI(
        title='projecto con database',
        version='1.1'
    )


    api.include_router(router, tags=['Welcome'])
    return api


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="debug", port=8001, reload=True)
