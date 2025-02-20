from api.serializers import *
from api.models import *
from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status

class BlogPostListCreate(APIView):

    def post(self, request, *args, **kwargs):

        # queryset = BlogPost.objects.all()

        # serialzer_class = BlogPostSerializer()
        return Response("Post api working ", status=status.HTTP_200_OK)


