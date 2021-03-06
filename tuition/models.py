from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=15)
    message = models.EmailField()

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    contact = models.CharField(max_length=50)
    message = models.EmailField()
    def __str__(self):
        return self.name
