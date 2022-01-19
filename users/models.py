from django.db import models

# Create your models here.
class user (models.Model):
    user_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Mobile = models.CharField(max_length=15)
    Roll = models.CharField(max_length=25)
    create_Data = models.DateField()


    def __str__(self):
        return self.user_Name