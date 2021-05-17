from django.db import models

# Create your models here.

class user_querry(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")

    def __srt__(self):
        return self.user_name