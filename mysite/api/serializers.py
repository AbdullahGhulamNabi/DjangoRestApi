from api.models import *
from rest_framework import serializers

class BlogPostSerializer(serializers.Serializer):
    class meta:
        model = BlogPost
        field = ['id','title','content','published_date']
