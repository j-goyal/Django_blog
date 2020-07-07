from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):   # used to show name of the object rather to show object1 or object2
        return "Message from " + self.name + " - " + self.email
    