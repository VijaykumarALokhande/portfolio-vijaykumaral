from django.db import models
class Tempo(models.Model):
    topic = models.CharField(max_length=250, default="goat")
    pubdate= models.DateTimeField()
    describe= models.TextField()
    image = models.ImageField(upload_to='Image/')

    def summary(self):
        return self.describe[:100]
    def custom_date(self):
        return self.pubdate.strftime('%b %e %Y')
    def __str__(self):
        return self.topic
