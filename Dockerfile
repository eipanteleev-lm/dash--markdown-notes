FROM python:3.7-slim-buster

WORKDIR /usr/app

ADD requirements.txt requirements.txt

RUN apt-get update \
  && apt-get install -y g++ \
  && python3.7 -m pip install --upgrade pip \
  && python3.7 -m pip install --no-cache -r requirements.txt \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base \
    ~/.cache/pip

COPY src src
COPY templates templates

ENTRYPOINT ["python3.7"]

CMD ["src/app.py"]