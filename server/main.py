import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from weather.router import weather_router


def create_server():
    app = FastAPI()
    
    # CORS 허용 설정
    origins = [
        "http://localhost:5173",  # 특정 도메인만 허용하고 싶을 때
        # "*"  # 모든 도메인을 허용하려면 이 줄을 사용합니다.
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # 허용할 origin 리스트
        allow_credentials=True,  # 쿠키 등을 포함한 자격 증명을 허용할지 여부
        allow_methods=["*"],  # 허용할 HTTP 메서드 (GET, POST, PUT, DELETE 등)
        allow_headers=["*"],  # 허용할 HTTP 헤더
    )

    app.include_router(weather_router)

    return app

app = create_server()

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)

