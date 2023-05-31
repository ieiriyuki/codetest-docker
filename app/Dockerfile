FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -U pip \
    && pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "4" ]
