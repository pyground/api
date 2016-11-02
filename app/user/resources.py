from utils.generic_resource import GenericResource
from user.models import User
from utils.generic_resource import router_build

user_routes = router_build(GenericResource(User), "user")
