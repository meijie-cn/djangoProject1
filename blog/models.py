from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,related_name='blog_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    creation_date = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['-creation_date','title']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def get_comments(self):
        return Comment.objects.filter(blog_id=self.id)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,related_name='comment_author',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comment_blog')
    reply = models.CharField(max_length=2000)
    creation_date = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.reply[0:10]
