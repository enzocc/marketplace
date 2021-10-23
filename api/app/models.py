from app.core.database import Base, db
__all__ = ["Base"]


class Products(Base):
    product_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
