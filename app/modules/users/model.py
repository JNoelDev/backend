from app.db.base import Base
from app.shared.models.base import UUIDStampz
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Text


class User(Base,UUIDStampz):

    __tablename__ = "users"

    fisrt_name : Mapped[str] = mapped_column(
        String(150),nullable=False,index=True
    )
    last_name : Mapped[str] = mapped_column(
        String(150),nullable=False,index=True
    )
    email : Mapped[str] = mapped_column(
        String(250),nullable=False,unique=True,index=True
    )
    hash_password : Mapped[str] = mapped_column(
        Text,nullable=False
    )
