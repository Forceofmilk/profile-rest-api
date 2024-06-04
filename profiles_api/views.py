from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiView = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tranditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            'Pizza is yummy'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiView})
