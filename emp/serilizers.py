from rest_framework import serializers
from emp import models
from emp.models import EmployeeModel


class Empserilizer(serializers.ModelSerializer):
    class Meta:
        Model = EmployeeModel
        fields = "__all__"
