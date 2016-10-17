from utils.generic_resource import GenericResource
from snippet.models import Snippet
from pynterpreter import Pynterpreter
from tornado import gen

class SnippetResource(GenericResource):
    def __init__(self):
        super().__init__(Snippet)

    @gen.coroutine
    def run_code(self):
        pntr = Pynterpreter()

        raise gen.Return({
            "response": pntr.run_as_module(self.request.GET["code"])
        })

snippet_additional_route = (r'api/snippet/run', SnippetResource.as_detail(), SnippetResource.run_code);

snippet_routes = router_build(User, "snippet").append(snippet_additional_route)
