from sqlalchemy import Column, Integer, String
from src.database import Base
from sqlalchemy.orm import Mapped, relationship


class Categorie(Base):
    __tablename__ = "categories"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, nullable=False, unique=True)
    slug: Mapped[str] = Column(String, unique=True, nullable=False)
    product = relationship("Product", back_populates="categorie")