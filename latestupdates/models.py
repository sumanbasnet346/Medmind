from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author =  models.CharField(max_length=255)
    # views = models.IntegerField(default=0)
    slug =  models.CharField(max_length=255)
    timeStamp = models.DateTimeField(blank = True)

    def __str__(self):
        return self.title + ' by '+ self.author

