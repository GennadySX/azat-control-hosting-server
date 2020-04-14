from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.core import serializers
import json
import os
from django.db.models import Q

class ApiDomainView(ListCreateAPIView, CreateModelMixin, UpdateModelMixin, DestroyModelMixin ):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer

    def perform_create(self, serializer):
        # send = DomainModel.objects.all().first()
        # os.system('cscript F:\\TEST\\run.vbs "F:\TEST\d.txt" "Robert" "' + self.request.data.get('conf') + '"')
        serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request)

    def update(self, serializer):
        r = serializer.data
        domain = DomainModel.objects.get(id=r.get('id'))
        domain.status = r.get('status')
        domain.save(update_fields=['status'])
        return Response({ "data": r.get('name')})

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        r_id = request.data.get('id')
        domain = DomainModel.objects.filter(id=r_id)
        if domain.exists():
            domain.delete()
            return Response({'status': True, 'deleted_id': r_id})
        else:
            return Response({'status': False, 'err': 'object not found'})

