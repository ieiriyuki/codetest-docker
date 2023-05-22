FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -U pip \
    && pip install -r requirements.txt

COPY . .

# ENTRYPOINT [ "uvicorn", "main:app", "--port", "8888" ]
