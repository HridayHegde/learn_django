from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=400)

    def __str__(self):
        return self.username
    
    def get_datalist(self):
        return [self.userid,self.username,self.password]