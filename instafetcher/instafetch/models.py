from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    secretPassword = models.CharField(max_length=50)

    def __str__(self):
        return self.email