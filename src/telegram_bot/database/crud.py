from sqlalchemy.orm import Session

from src.telegram_bot.database import models
from src.database import session


def add_data_new_group(chat, update, db: Session = session()):
    db_group = models.TelegramGroups(
        chat_id=chat,
        update_id=update,
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def get_data_groups(db: Session = session(), ofset=0, limit=100):
    return db.query(models.TelegramGroups).offset(ofset).limit(limit).all()
