from djongo import models

# Create your models here.


class Image(models.Model):
    _id = models.ObjectIdField()
    imageUrl = models.TextField()
    user_id = models.EmailField()
