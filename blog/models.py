from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    postimage = models.ImageField(upload_to='images/', default='')
    blogpost = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.blogpost[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')