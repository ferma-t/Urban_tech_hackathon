from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from hackathon.settings import UPLOAD_ROOT, UPLOAD_URL
from django.core.files.storage import FileSystemStorage

# upload settings
upload_storage = FileSystemStorage(location=UPLOAD_ROOT, base_url=UPLOAD_URL)
def upload_to_path(instance, filename):
    return  'doc_template_{%s}/{%s}' % (instance.id, filename)

class HackathonBase(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField('Дата создания', auto_now_add=True)

class HackathonDictionary(HackathonBase):
    class Meta:
        abstract = True

    name = models.CharField('Наименование', max_length=255)


class DocumentTypes(HackathonDictionary):
    class Meta:
        db_table = 'document_types'
        verbose_name = 'Типы документов'
        verbose_name_plural = 'Типы документов'

    description = models.TextField('Описание типа документа', null=True, blank=False, )
    template_file = models.FileField('Шаблон документа', null=True, upload_to=upload_to_path, storage=upload_storage)

    def __str__(self):
        return self.name


class Document(HackathonBase):
    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    type = models.ForeignKey(DocumentTypes, verbose_name = 'Тип документа', on_delete=models.PROTECT)
    number = models.CharField('Номер', max_length=255)
    creation_date = models.DateTimeField('Дата создания', null=True, blank=True)
    approval_date = models.DateTimeField('Дата утверждения', null=True, blank=True)
    institute = models.ForeignKey('Institute', on_delete=models.PROTECT, verbose_name='Организация')
    to_institute = models.ForeignKey('Institute', verbose_name='Получатель', null=True, default=None, blank=True, on_delete=models.PROTECT,  related_name = 'document_institute_to')

    def __str__(self):
        return '%s (%s)' % (self.type.name, self.number)


class Institute(HackathonDictionary):
    class Meta:
        db_table = 'institute'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    INSTITUTE_TYPE_CHOICES = [('BUDGET_INSTITUTE', 'Бюджетная организация'),
                             ('AUTONOMOUS_INSTITUTE', 'Автономная организация'),
                             ('PUBLIC_INSTITUTE', 'Казенное учреждение'),
                             ('GOVERNMENT_INSTITUTE', 'Государственное унитарное предприятие'),
                             ]

    TIN = models.CharField('ИНН учреждения', max_length=12, blank=True)
    founder = models.ForeignKey('Institute', on_delete=models.SET_NULL, verbose_name = 'Родительское ведомство', null=True, blank=True)
    institute_type = models.CharField(max_length=255, choices = INSTITUTE_TYPE_CHOICES)
    description = models.TextField("Описание учреждения", null=True, blank=True, default='')

    def __str__(self):
        return self.name


class BaseProcess(HackathonDictionary):
    class Meta:
        db_table = 'base_process'
        verbose_name = 'Шаблон процесса'
        verbose_name_plural = 'Шаблон процесса'
        verbose_name_plural = 'Шаблоны процесса'

    parent_process = models.ForeignKey('BaseProcess', verbose_name='Родитель', blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField("Описание процесса", null=True, blank=True, default='')

    def __str__(self):
        return self.name


class Process(HackathonBase):
    class Meta:
        db_table = 'process'
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процесы'

    STATUS_CHOICES = [('DONE', 'Сделано'),
                    ('OVERDUE', 'Просрочены'),
                    ('IN_PROCESS', 'Нужно сделать'),]

    process = models.ForeignKey('BaseProcess', null=False, on_delete=models.PROTECT)
    from_institute = models.ForeignKey(Institute, verbose_name='Отправитель', on_delete=models.PROTECT, related_name = 'institute_from')
    to_institute = models.ForeignKey(Institute, verbose_name='Получатель', on_delete=models.PROTECT,  related_name = 'institute_to')
    document_type = models.ManyToManyField(DocumentTypes, verbose_name = 'Тип документа')
    period = models.ForeignKey('Period', verbose_name='Период планирования', on_delete=models.SET_NULL, null=True, default=None)
    start_date = models.DateField(null=True, default=None)
    expiration_date = models.DateField(null=True, default=None)
    law_base = models.TextField('Законное основание', null=False, blank=False)
    description = models.TextField("Описание процесса", null=True, blank=True, default='')
    status = models.CharField(max_length=255, choices = STATUS_CHOICES, null=True, blank=True, default='IN_PROCESS')

    def __str__(self):
        return self.process.name
    

class UserInstitutes(HackathonBase):
    class Meta:
        db_table = 'users_institutes'
        verbose_name = u'Организации пользователя'
        verbose_name_plural = u'Организации пользователя'
    
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    institutes = models.ManyToManyField('Institute', verbose_name='Доступные организации')
    description = models.TextField("Описание процесса", null=True, blank=True, default='')

    def __str__(self):
        return self.user.username


class Period(HackathonDictionary):
    class Meta:
        db_table = 'periods'
        verbose_name = 'Периоды'
        verbose_name_plural = 'Периоды'
    
    start_date = models.DateField(null=True, default=None)
    expiration_date = models.DateField(null=True, default=None)

    def __str__(self):
        return self.name
