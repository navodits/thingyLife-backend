from djongo import models
from photographs.models import Image

# Create your models here.


class Post(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    datePosted = models.DateField(auto_now=True)
    liked = models.BooleanField()
    user_id = models.EmailField()
