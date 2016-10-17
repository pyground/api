from utils.generic_resource import GenericResource
from snippet.models import Snippet

class SnippetResource(GenericResource):
    def __init__(self)
        super().__init__(Snippet)

snippet_routes = router_build(User, "snippet")
