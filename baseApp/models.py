from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Developers(models.Model): # one_to_many relationship (developer can work in many companies at a time)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)  # SET_NULL mean advocate will not be deleted
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username