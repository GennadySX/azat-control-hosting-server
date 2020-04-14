from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.response import Response
from .serializers import *
import os


def removeIt(domain, also=None):
    os.system(f'rm -rf /etc/nginx/sites-enabled/{domain}')
    if(also != None):
        os.system(also)
    os.system(f'timeout 5s systemctl restart nginx')


def activateIt(domain):
    os.system(f'ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/')
    os.system(f'timeout 5s systemctl restart nginx')


class ApiDomainView(ListCreateAPIView, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer



    def perform_create(self, serializer):
        project_name = self.request.data.get("name")
        os.system(f'cp ./conf /etc/nginx/sites-available/{project_name}')
        os.system(
            f'sudo sed -i -e "s/app_name/{project_name}/" -e "s/port/{self.request.data.get("port")}/"'
            f' /etc/nginx/sites-available/{project_name}')
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
        if (r.get('status') > 1):
            activateIt(domain=domain.name)
            return Response({'status': True, "domain": r.get('name')})
        else:
            removeIt(domain=domain.name)
            return Response({'status': True, "domain": r.get('name')})
        return Response({'status': False, "err": 'domain conf file not found'})

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        r_id = request.data.get('id')
        name = request.data.get('name')
        domain = DomainModel.objects.filter(id=r_id)
        if domain.exists():
            removeIt(domain=name, also=f"rm -rf /etc/nginx/sites-available/{name}")
            domain.delete()
            return Response({'status': True, 'deleted_id': r_id})
        else:
            return Response({'status': True, 'err': 'object not found'})
