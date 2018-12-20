from django.http import HttpResponse,HttpRequest
from api.drawgraphs.mock_graph import draw_mock_graph
from .view import KMCGraph

class MockPicture(KMCGraph):
    def get(self, request, format=None):
        
        parameters ={'locale':'en'}
        return self.draw_graph(parameters)
    
    def draw_graph(self, parameters, isdebug = False):
        
        pil_image = draw_mock_graph()

        response = HttpResponse(content_type="image/png")
        pil_image.save(response,"PNG")

        return response