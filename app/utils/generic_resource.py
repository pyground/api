from tornado import gen
from restless.tnd import TornadoResource

class GenericResource(TornadoResource):
    def __init__(self, instance):
        super().__init__()
        self._instance = instance

    def _get_one(self, pk):
        return self._instance.objects(id=pk)[0]

    @gen.coroutine
    def list(self):
        users = self._instance.objects()
        raise gen.Return(users)

    @gen.coroutine
    def details(self, pk):
        user = self._get_one(pk)
        return gen.Return(user)

    @gen.coroutine
    def create(self):
        user = self._instance(**self.request.GET)
        raise gen.Return(user.save())

    @gen.coroutine
    def update(self, pk):
        user = self._get_one(pk)

        for key, value in self.request.GET
            user[key] = value

        raise gen.Return(user.save())

    @gen.coroutine
    def delete(self, pk):
        user = self._get_one(pk);
        raise gen.Return(user.delete())
