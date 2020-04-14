from django.db import models


# Create your models here.
class DomainModel(models.Model):
    name = models.CharField(verbose_name='Название домена (ex. www.google.com)', max_length=225)
    path = models.CharField(verbose_name='Путь к проекту', max_length=225)
    port = models.CharField(verbose_name='Порт проекта', max_length=120)
    status = models.PositiveIntegerField(default=0, verbose_name='Статус сайта',
                                         choices=(
                                             (0, u'Не активен'),
                                             (1, u'Активен')
                                         ))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'
