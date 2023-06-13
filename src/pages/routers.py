from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.products.routers import get_product

router_pages = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")

@router_pages.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router_pages.get("/search/{product_name}")
def get_search_page(request: Request, products=Depends(get_product)):
    return templates.TemplateResponse("product.html", {"request": request, "products": products[0]})