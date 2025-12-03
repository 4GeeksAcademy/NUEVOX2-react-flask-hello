from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_passwor_hash

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeingKey, Text, DateTime, Integer


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Stting(120), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates='user', cascade='all, delete-orphan')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


