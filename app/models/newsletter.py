from datetime import datetime
from sqlalchemy import func
from app.db import db
from sqlalchemy_serializer import SerializerMixin 
from sqlalchemy.orm import Mapped,mapped_column

class Newsletter(db.Model,SerializerMixin):
    __tablename__="newsletters"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]
    body:Mapped[str]
    published_at:Mapped[datetime]=mapped_column(server_default=func.now())
    edited_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdae=func.now())

    def __repr__(self):
        return f"<Newsletter {self.title} published at {self.published_at}>"