FROM python:3.11-slim-bullseye AS base

WORKDIR /app

RUN apt-get update && apt-get -y upgrade

COPY ./server/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./server ./

ENTRYPOINT ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "8000"]
