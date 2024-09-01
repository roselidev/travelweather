FROM python:3.11-slim-bullseye AS base

WORKDIR /app

RUN apt-get update && apt-get -y upgrade

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "9000", "--workers", "4"]
