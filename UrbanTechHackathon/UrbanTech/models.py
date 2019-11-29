"""
Definition of models.
"""

from django.db import models

class HackatonBase(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField('Дата создания')


class Document(HackatonBase):
    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    type = models.CharField('Тип документа', max_length=255)
    number = models.CharField('Номер', max_length=255)
    creation_date = models.DateTimeField('Дата создания')
    approval_date = models.DateTimeField('Дата утверждения')
    founder_TIN = models.CharField('ИНН учредителя', max_length=12, blank=True)
    facilty_TIN = models.CharField('ИНН учреждения', max_length=12, blank=True)





