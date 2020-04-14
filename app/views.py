from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.core import serializers
import json
import os


class ApiDomainView(ListCreateAPIView, CreateModelMixin, UpdateModelMixin, DestroyModelMixin ):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer

    def perform_create(self, serializer):
        # send = DomainModel.objects.all().first()
        # os.system('cscript F:\\TEST\\run.vbs "F:\TEST\d.txt" "Robert" "' + self.request.data.get('conf') + '"')
        serializer.save()

    def get_(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def get(self, request):
        return Response(json.loads(serializers.serialize("json", DomainModel.objects.all())))

    def put(self, request, *args, **kwargs):
        return self.update(request)

    def update(self, serializer):
        r = serializer.data
        domain = DomainModel.objects.get(id=r.get('id'))
        domain.status = r.get('status')
        domain.save(update_fields=['status'])
        return Response({ "data":serializer.data.get('name')})

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
