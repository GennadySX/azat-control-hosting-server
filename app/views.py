from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.core import serializers
import json
import os


# Create your views here.
class ApiProjectView(ListCreateAPIView):
    queryset = ProjectTypeModel.objects.all()
    serializer_class = ProjectTypeSerializer

    def perform_create(self,  serializer):
        send = ProjectTypeModel.objects.all().first()
        print('ds')
        os.system('cscript F:\\TEST\\run.vbs "F:\TEST\d.txt" "Robert" "'+self.request.data.get('conf')+'"')
        serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)


    def delete(self, request, pk):
        project = get_object_or_404(ProjectTypeModel.objects.all(), pk=pk)
        project.delete()
        return project


class ApiDomainView(ListCreateAPIView):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer

    def get(self, request):
        return Response(json.loads(serializers.serialize("json", DomainModel.objects.all())))

    def set(self, request):
        return Response(json.loads(request.data))

    def delete(self, request, pk):
        domain = get_object_or_404(DomainModel.objects.all(), pk=pk)
        domain.delete()
        return domain
