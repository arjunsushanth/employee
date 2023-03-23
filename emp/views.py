from django.shortcuts import render
from rest_framework.views import APIView
from emp.models import EmployeeModel
from rest_framework.views import Response
from rest_framework import viewsets
from emp.serilizers import Empserilizer


class EmployeeView(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = Empserilizer


