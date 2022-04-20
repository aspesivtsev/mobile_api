from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from .models import Attraction
from .serializers import AttractionSerializer

class AttractionAPIView(APIView):
    """Show all attractions"""
    def get(self, request):
        attractions = Attraction.objects.all().filter(is_active=True)
        serializer = AttractionSerializer(attractions, many=True,)

        return Response(serializer.data)
'''



from rest_framework import generics
class AttractionAPIView(generics.ListAPIView):
    queryset = Attraction.objects.all().filter(is_active=True)
    serializer_class = AttractionSerializer
'''