import redis

from tornado import web, ioloop
from itertools import chain
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB
from user.resources import user_routes
from snippet.resources import snippet_routes

routes = chain(
    user_routes,
    snippet_routes
)

Redis = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB
)

app = web.Application(routes, debug=True)

if __name__ == '__main__':
    app.listen(8001)
    ioloop.IOLoop.instance().start()
