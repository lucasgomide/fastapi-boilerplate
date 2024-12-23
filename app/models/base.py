from sqlmodel import Field, SQLModel
from datetime import datetime, UTC
from sqlalchemy import event


class BaseModel(SQLModel):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(tz=UTC))


@event.listens_for(BaseModel, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(tz=UTC)
