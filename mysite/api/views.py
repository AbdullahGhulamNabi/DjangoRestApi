from api.serializers import *
from api.models import *
from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status

class BlogPostListCreate(APIView):

    def post(self, request):

        blog_data = request.data

        blog_title = blog_data['title']
        blog_content = blog_data['content']
        # print(title, content)

        if BlogPost.objects.filter(title=blog_title).exists():
            return Response({'error': 'Blog with same title already exists'}, status=status.HTTP_400_BAD_REQUEST)
        

        blog = BlogPost.objects.create(title=blog_title, content=blog_content)
        serialized_data = BlogPostSerializer(blog)

        return Response(serialized_data.data,status=status.HTTP_200_OK)
    
    def get(self, request):

        blog_title = request.query_params.get('title')

        try:
            queryset = BlogPost.objects.get(title = blog_title)

        except BlogPost.DoesNotExist:
            return Response({'error':'Blog post not found'}, status=status.HTTP_400_BAD_REQUEST)

        print(queryset)

        serialized_data = BlogPostSerializer(queryset)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    



