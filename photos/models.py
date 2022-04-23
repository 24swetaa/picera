from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

class Feedback(models.Model):
    First_Name = models.CharField(max_length = 120)
    Last_Name = models.CharField(max_length = 120)
    Email = models.EmailField()
    Phone_Number = models.IntegerField()
    Help = models.TextField()

    def __str__(self):
        return self.First_Name