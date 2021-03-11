from django.db import models
class Tempo(models.Model):
    topic = models.CharField(max_length=250, default="goat")
    pubdate= models.DateTimeField()
    describe= models.TextField()
    image = models.ImageField(upload_to='Image/')
