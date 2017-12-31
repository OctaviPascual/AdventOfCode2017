FROM python:3.5-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /opt/adventOfCode
WORKDIR /opt/adventOfCode

ADD adventofcode .

ENTRYPOINT [ "python", "adventofcode.py" ]
