from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Uuid,text,DateTime,func
from datetime import datetime
import uuid


class UUIDStampz:
    
    id : Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
        nullable=False
    )

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        nullable=False
    )

    updated_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now,
        server_default=func.now(),
        nullable=False
    )