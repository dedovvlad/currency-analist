import json
from datetime import timedelta

import redis

import settings


class Redis:
    def __init__(self, redis_host, redis_port: None, brunch: tuple = None):
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__brunch = brunch

    @property
    def _client_redis(self):
        client = redis.Redis(
            host=self.__redis_host,
            port=self.__redis_port,
        )
        return client

    def _add_branch(self, key):
        return (":".join(self.__brunch) + ":" + key) if self.__brunch else key

    def get_item(self, key):
        return self._client_redis.get(self._add_branch(key))

    def setex_item(self, key, item, time_cache=settings.TIME_CACHE):
        return self._client_redis.setex(
            name=self._add_branch(key),
            value=json.dumps(item),
            time=timedelta(seconds=time_cache),
        )

a = ("currency", "test")
b = "path"
print("/".join(a) + "/" + b)