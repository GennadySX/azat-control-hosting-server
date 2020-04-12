from django.db import models

# Create your models here.


class ProjectTypeModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название проекта')
    conf = models.TextField(verbose_name='Конфиг текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип проекта'
        verbose_name_plural = 'Типы проектов'


class DomainModel(models.Model):
    name = models.CharField(verbose_name='Название домена (ex. www.google.com)', max_length=225)
    path = models.CharField(verbose_name='Путь к проекту', max_length=225)
    static = models.CharField(verbose_name='Название статической папке', max_length=120)
    status = models.PositiveIntegerField(default=0, choices=((0, u'Не активен'),(1, u'Активен')), verbose_name='Статус сайта')
    server = models.PositiveIntegerField(default=0, choices=(
        (0, u'Apache'),
        (1, u'Nginx')
    ), verbose_name='Типы сервера')
    projectType = models.ForeignKey(ProjectTypeModel, verbose_name='Типы проекта', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'
