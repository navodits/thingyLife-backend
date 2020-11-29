from djongo import models

# Create your models here.

class Post(models.Model):
    _id = models.ObjectIdField()
    photo = models.ImageField()
    user_id = models.EmailField()

