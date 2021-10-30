from django.db import models

class Post(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    short = models.TextField(max_length=280)
    title = models.CharField(max_length=200)
