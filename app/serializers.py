from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import fields
from .models import *


class ProjectTypeSerializer(serializers.ModelSerializer):


    def update(self, instance, validated_data):
        instance.save()
        return instance

    class Meta:
        fields = ('name','conf', )
        model = ProjectTypeModel


class DomainSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DomainModel.save(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

    def delete(self, request):
        domain = get_object_or_404(DomainModel.objects.all())
        domain.delete()
        return domain

    class Meta:
        fields = (
            'id',
            'name',
            'path',
            'static',
            'status',
            'server',
            'projectType',
        )
        model = DomainModel
