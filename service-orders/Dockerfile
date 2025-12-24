FROM python:3.12-slim

WORKDIR /app

# ⬇️ DİKKAT: path verdik
COPY service-orders/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY service-orders/app ./app
COPY service-orders/app/templates ./templates
COPY shared/ui ./shared/ui

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
