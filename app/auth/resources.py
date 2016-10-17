import uuid

from app import Redis
from tornado import gen
from restless.tnd import TornadoResource

class AuthResource(TornadoResource)
    @gen.coroutine
    def create(self):
        user = User.objects(**self.request.GET)
        uid = str(uuid.hex())
        raise gen.Return(Redis.set(uid, user))

    @gen.coroutine
    def delete(self, pk):
        raise gen.Return(Redis.get(pk))


    @gen.coroutine
    def detail(self, pk):
        raise gen.Return(Redis.get(pk))
