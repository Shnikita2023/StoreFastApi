from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    slug: str
    price: float
    image: str
    article: str
    categorie_id: int
    brand_id: int

    class Config:
        orm_mode = True

class GetProduct(CreateProduct):
    id: int

