import os
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

CATALOG_URL = os.getenv("CATALOG_URL", "http://service-catalog:8001")

app = FastAPI(title="Orders API", version="1.0.0", description="Stateless orders microservice (calls catalog)")

app.mount("/static", StaticFiles(directory="/app/shared/ui/static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(req: Request):
    return templates.TemplateResponse("index.html", {"request": req, "catalog_url": CATALOG_URL})

@app.get("/health")
def health():
    return {"ok": True, "service": "orders", "catalog": CATALOG_URL}

@app.get("/quote/{product_id}")
async def quote(product_id: str, qty: int = 1):
    # Stateless: Her istekte catalog'dan ürün çekip fiyat hesaplar
    async with httpx.AsyncClient(timeout=5) as client:
        r = await client.get(f"{CATALOG_URL}/products/{product_id}")
        data = r.json()

    if "id" not in data:
        return {"detail": "Product not found", "product_id": product_id}

    total = float(data["price"]) * int(qty)
    return {"product": data, "qty": qty, "total": total}
