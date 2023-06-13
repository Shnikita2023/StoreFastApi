from pydantic import BaseModel


class CreateBrand(BaseModel):
    name: str
    slug: str

    class Config:
        orm_mode = True

class GetBrand(CreateBrand):
    id: int


