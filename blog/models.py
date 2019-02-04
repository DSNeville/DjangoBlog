from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    pub_date = models.TimeField(auto_now=True)
    postimage = models.ImageField(upload_to='images/', default='')
    blogpost = models.TextField()