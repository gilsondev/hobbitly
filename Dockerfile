FROM python:3.10-alpine as hobbitly-base

ENV PYTHONUNBUFFERED 1
ENV PIP_TIMEOUT 60
ENV PYTHONPATH $PYTHONPATH:/usr/src/app
ENV POETRYPATH /root/.local/bin
ENV PATH $POETRYPATH:$PATH
ENV APP_HOME /home/app

RUN apk add --update --no-cache curl gcc libc-dev \
    linux-headers zlib zlib-dev musl-dev libffi-dev \
    openssl-dev python3-dev make build-base

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# Create user and directory
RUN mkdir -p ${APP_HOME}
RUN addgroup -S app && adduser -S app -G app

WORKDIR ${APP_HOME}
COPY . ${APP_HOME}
RUN chown -R app:app ${APP_HOME}

RUN poetry config virtualenvs.create false

FROM hobbitly-base as hobbitly-dev

RUN poetry install

USER app

CMD ["uvicorn", "src.app:app", "--host=0.0.0.0", "--port=8000", "--reload"]

FROM hobbitly-base as hobbitly

RUN poetry install --no-dev

USER app

CMD ["uvicorn", "src.app:app", "--host=0.0.0.0", "--port=8000"]

