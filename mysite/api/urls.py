from django.urls import path
from api.views import *

urlpatterns = [

    path('blog-post/', BlogPostListCreate.as_view(), name="create-blog-post")
]
