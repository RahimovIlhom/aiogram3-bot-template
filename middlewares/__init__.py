import asyncio

from aiogram import Router
from aioredis import Redis

from middlewares.throttling import ThrottlingMiddleware

loop = asyncio.get_event_loop()
redis_instance = Redis.from_url("redis://localhost", loop=loop)

router = Router()
router.message.middleware(ThrottlingMiddleware(redis_instance))
