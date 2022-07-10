import json
from datetime import timedelta

from redis import Redis

from src import settings

client_redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
)


def get_item_from_redis(item):
    return client_redis.get(item)


def setex_item_to_redis(key, item):
    client_redis.setex(
        name=key,
        value=json.dumps(item),
        time=timedelta(seconds=settings.TIME_CACHE),
    )
