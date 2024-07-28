import uvicorn
from fastapi import FastAPI

from weather.router import weather_router


def create_server():
    app = FastAPI()

    app.include_router(weather_router)

    return app

app = create_server()

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)

