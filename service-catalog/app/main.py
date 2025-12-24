from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(title="Catalog API", version="1.0.0", description="Stateless catalog microservice")

# shared ui mounted into image at /app/shared/ui
app.mount("/static", StaticFiles(directory="/app/shared/ui/static"), name="static")
templates = Jinja2Templates(directory="templates")

# Stateless sample data (hardcoded)
PRODUCTS = [
    {"id": "p-100", "name": "Keyboard", "price": 49.9},
    {"id": "p-200", "name": "Mouse", "price": 19.9},
    {"id": "p-300", "name": "Monitor", "price": 179.0},
]

@app.get("/", response_class=HTMLResponse)
def home(req: Request):
    return templates.TemplateResponse("index.html", {"request": req, "service": "catalog"})

@app.get("/health")
def health():
    return {"ok": True, "service": "catalog"}

@app.get("/products")
def list_products():
    return {"items": PRODUCTS}

@app.get("/products/{product_id}")
def get_product(product_id: str):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return {"detail": "Not Found"}
