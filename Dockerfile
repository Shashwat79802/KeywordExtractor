FROM python:3.10-bullseye

WORKDIR /keyword_extractor

ENV PYTHONUBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /keyword_extractor/requirements.txt

COPY ./gunicorn_conf.py /keyword_extractor/gunicorn_conf.py

RUN pip install --no-cache-dir --upgrade -r /keyword_extractor/requirements.txt

COPY ./app /keyword_extractor/app

RUN mkdir -p /tmp/shm

COPY ./.env /keyword_extractor/.env

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_conf.py", "app.main:app"]