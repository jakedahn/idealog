from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Idea
from serializers import IdeaSerializer


class IdeaList(APIView):
    """
    List all api, or create a new idea.
    """
    def get(self, request, format=None):
        api = Idea.objects.all()
        serializer = IdeaSerializer(api, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
