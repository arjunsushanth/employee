from django.db import models

class EmployeeModel(models.Model):
     id=models.PositiveIntegerField(primary_key=True)
     name=models.CharField(max_length=100)
     salary=models.PositiveIntegerField(max_length=100)

