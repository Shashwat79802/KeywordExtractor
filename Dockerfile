FROM python:3.12.2-slim-bookworm

WORKDIR /keyword_extractor

ENV PYTHONUBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt ./gunicorn_conf.py ./

RUN python3 -m pip install -r ./requirements.txt

COPY . /keyword_extractor/

RUN mkdir -p /tmp/shm && mkdir /.local

ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_conf.py", "app.main:app"]
