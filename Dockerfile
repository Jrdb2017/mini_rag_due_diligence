FROM python:3.10-slim

WORKDIR /app

COPY ./app /app
COPY ./docs /app/docs
COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
