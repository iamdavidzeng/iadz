#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.db import models


class Demo(models.Model):
    a = models.CharField(max_lengt=8)
    b = models.CharField(min_length=2)


class CustomizeSerializer(serializers.ModelSerializer):

    def validate_a(self):
        return self.initial_data['a']
    
    def validate_b(self):
        return self.initial_data['b']

    class Meta:
        model = Demo
        fields = ('a', 'b')