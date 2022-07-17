from sqlalchemy.orm import Session

from src.utils.database import session
from src.telegram_bot.database import models


def add_data_new_group(id_chat, title_chat, type_chat, db: Session = session()):
    add_chat_data = models.TelegramGroups(
        id_chat=id_chat,
        title=title_chat,
        type=type_chat,
    )
    db.add(add_chat_data)
    db.commit()
    db.refresh(add_chat_data)
    return add_chat_data


def get_data_groups(db: Session = session(), ofset=0, limit=100):
    return db.query(models.TelegramGroups).offset(ofset).limit(limit).all()
