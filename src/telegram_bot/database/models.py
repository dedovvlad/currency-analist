from sqlalchemy import Boolean, Column, Integer, String

from src.database import Base


class TelegramGroups(Base):
    __tablename__ = "telegram_groups"
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, unique=True, index=True)
    update_id = Column(String, unique=True, index=True)
