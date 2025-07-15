from django.db import models


# Create your models here.
class Browse(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="browse/")
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contact(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email


class TopicListing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="topiclisting/")
    about = models.TextField()

    def __str__(self):
        return self.name
