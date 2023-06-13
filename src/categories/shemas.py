from pydantic import BaseModel


class CreateCategorie(BaseModel):
    name: str
    slug: str

    class Config:
        orm_mode = True

class GetCategorie(CreateCategorie):
    id: int


