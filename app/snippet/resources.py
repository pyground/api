from utils.generic_resource import GenericResource, router_build
from snippet.models import Snippet
from core.pynterpreter import Pynterpreter
from tornado import gen

class SnippetResource():
    @gen.coroutine
    def detail(self):
        pntr = Pynterpreter()

        raise gen.Return({
            "response": pntr.run_as_module(self.request.GET["code"])
        })

snippet_additional_route = (r'api/run_snippet', SnippetResource());

snippet_routes = router_build(GenericResource(Snippet), "snippet").append(snippet_additional_route)
