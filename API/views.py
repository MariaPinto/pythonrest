# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from API.models import Person
from API.serializers import UserSerializer


class Personas(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = UserSerializer


class PersonasDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Person.objects.all()
    serializer_class = UserSerializer