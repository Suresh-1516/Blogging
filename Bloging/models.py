from django.db import models
from ckeditor.fields import RichTextField

class Blogpost(models.Model):
    blog_user = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default="Other")
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True,null=True) 

    def __str__(self):
        return self.title


class Like(models.Model):
    liked_blog_user = models.CharField(max_length=100)
    liked_blog_id = models.CharField(max_length=100)

    def __str__(self):
        return self.liked_blog_user


class Comment(models.Model):
    comment_user = models.CharField(max_length=100)
    comment_string = models.CharField(max_length=100,default=None)
    comment_blog_id = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_user
