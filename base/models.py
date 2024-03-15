from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)    



class UserCheckpoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkpoint_name = models.CharField(max_length=100)
    checkpoint_url_endpoint = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
