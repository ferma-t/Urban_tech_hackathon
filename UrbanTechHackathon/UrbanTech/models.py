"""
Definition of models.
"""

from django.db import models

class HackathonBase(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField('Дата создания')


class Document(HackathonBase):
    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    type = models.CharField('Тип документа', max_length=255)
    number = models.CharField('Номер', max_length=255)
    creation_date = models.DateTimeField('Дата создания')
    approval_date = models.DateTimeField('Дата утверждения')
    instatute = models.ForeignKey('Institute',on_delete=models.PROTECT, verbose_name='Организация')


class Institute(HackathonBase):
    class Meta:
        db_table = 'institute'
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждение'

    name = models.CharField('Наименование', max_length=255)
    TIN = models.CharField('ИНН учреждения', max_length=12, blank=True)
    founder = models.ForeignKey('Founder', on_delete=models.SET_NULL, verbose_name = 'Учредитель', null=True, blank=True)


class Founder(HackathonBase):
    class Meta:
        db_table = 'founder'
        verbose_name = 'Учредитель'
        verbose_name_plural = 'Учредитель'
    
    name = models.CharField('Наименование', max_length=255)
    TIN = models.CharField('ИНН', max_length=12, blank=True)
    





