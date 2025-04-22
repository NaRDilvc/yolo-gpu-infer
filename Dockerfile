FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
