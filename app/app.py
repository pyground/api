import redis

# TODO: Extract values to settings
Redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# TODO: Routes <3
# import tornado.ioloop
#
# app = web.Application(routes, debug=True)
#
# if __name__ == '__main__':
#     app.listen(8001)
#     tornado.ioloop.IOLoop.instance().start()
