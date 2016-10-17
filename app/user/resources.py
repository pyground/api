from utils.generic_resource import GenericResource
from user.models import User
from utils.generic_resource import router_build

class UserResource(GenericResource):
    def __init__(self)
        super().__init__(User)

user_routes = router_build(User, "user")
