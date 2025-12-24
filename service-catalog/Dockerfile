FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY app/templates ./templates

# shared ui (from repo root shared/ui) will be copied by build context in compose
COPY shared/ui ./shared/ui

EXPOSE 8001
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
