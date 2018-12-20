from rest_framework.views import APIView

class KMCGraph(APIView):
    '''
        Base class for creating graph.
    '''
    def get(self, request, format=None):
        '''
            draw the graph and return a image response.
        '''