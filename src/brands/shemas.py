from pydantic import BaseModel


class CreateBrand(BaseModel):
    name: str
    slug: str

class GetBrand(CreateBrand):
    id: int

