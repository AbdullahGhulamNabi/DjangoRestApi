from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{'Title of blog',self.title}'