from django.db import models

class emp(models.Model):
    name = models.CharField(max_length = 50)
    salary = models.IntegerField()
    designation = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
# Create your models here.
