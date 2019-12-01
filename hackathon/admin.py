# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.register(DocumentTypes)
admin.site.register(Document)
admin.site.register(UserInstitutes)
admin.site.register(Period)


# расширение модели процесса
class BaseProcessInline(admin.StackedInline):
    model = BaseProcess
    verbose_name_plural = 'Дочерние процессы'
    extra = 1


class InstituteInline(admin.StackedInline):
    model = Institute
    verbose_name_plural = 'Дочерние организации(учреждения)'
    extra = 1


class BaseProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_process',)
    search_fields = ['name',]
    inlines = (BaseProcessInline,)          
admin.site.register(BaseProcess, BaseProcessAdmin)


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('process', 'from_institute', 'to_institute',)
    search_fields = ['process',]
admin.site.register(Process, ProcessAdmin)


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'founder',)
    search_fields = ['name',]
    inlines = (InstituteInline,)
admin.site.register(Institute, InstituteAdmin)
