FROM python:3.7.2-alpine

RUN pip install --upgrade pip
RUN apk add gcc musl-dev build-base postgresql-libs postgresql-dev

RUN adduser -D worker
USER worker
WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"
COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=worker:worker . .

CMD  [ "python3", "./app.py"]
