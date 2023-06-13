from sqlalchemy import Column, Integer, String, Float, ForeignKey, MetaData
from src.database import Base
from sqlalchemy.orm import Mapped, relationship
from src.categories.models import Categorie

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, nullable=False, unique=True)
    slug: Mapped[str] = Column(String, unique=True, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    article: Mapped[str] = Column(String, nullable=False)
    image: Mapped[str] = Column(String)
    categorie_id: Mapped[int] = Column(Integer, ForeignKey("categories.id"))
    brand_id: Mapped[int] = Column(Integer, ForeignKey("brands.id"))
    categorie = relationship("Categorie", back_populates="product")
    brand = relationship("Brand", back_populates="product")