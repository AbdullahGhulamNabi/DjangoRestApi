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
    

    def delete(self, request):
        try:
            blog_id = request.query_params.get('id')
            blog_to_delete = BlogPost.objects.get(id = blog_id)
            blog_to_delete.delete()
            return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except BlogPost.DoesNotExist:
            return Response({'error':'Blog Post Not found'}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request):

        try:
            blog_id = request.query_params.get('id')
            blog = BlogPost.objects.get(id= blog_id)

            updated_content = request.data.get('title')
            updated_title = request.data.get('content')


            blog.title = updated_title
            blog.content = updated_content


            serialized_data = BlogPostSerializer(blog,data=request.data, partial=True)
            if serialized_data.is_valid():
                blog.save()
                return Response({'message':'Blog post updated successfully'}, status=status.HTTP_200_OK)
        
        except BlogPost.DoesNotExist:
            return Response({'error':'Blog Post Not found'}, status=status.HTTP_404_NOT_FOUND)




