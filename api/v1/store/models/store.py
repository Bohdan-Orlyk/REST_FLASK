from db import db

from sqlalchemy.orm import Mapped, mapped_column


class StoreModel(db.Model):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
