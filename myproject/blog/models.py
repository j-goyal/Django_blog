from django.db import models

# Create your models here.

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)


    def __str__(self):   # used to show name of the object rather to show object1 or object2
        return self.title + "  By " + self.author
    