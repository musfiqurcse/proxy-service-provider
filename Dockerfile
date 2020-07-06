FROM python:3.7.8-alpine3.11
MAINTAINER md_musfiqur_rahman


ENV PYTHONUNBUFFERED 1

RUN \
    apk add --no-cache python3-pip python3-dev libpq-dev

RUN \
    python3 -m pip install --no-cache-dir Cython

COPY ./requirement.txt /requirement.txt
RUN \
 apk add --no-cache python3 postgresql-libs&& \
 apk add --no-cache libxml2-dev libxslt-dev python-dev && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirement.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D user
USER user


