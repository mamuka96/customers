from django.db import models

class Professions(models.Model):
    profession_name = models.CharField(max_length=30)

class Customers(models.Model):

    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=40)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    professions = models.ForeignKey(Professions, models.PROTECT)

