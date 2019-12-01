from rest_framework import serializers
import json

from hackathon.models import *


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTypes
        fields = '__all__'

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class UserInstitutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInstitutes
        fields = '__all__'

class BaseProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProcess
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ProcessSerializer(serializers.ModelSerializer):

    process = BaseProcessSerializer()
    from_institute = InstituteSerializer(many=False)
    to_institute = InstituteSerializer(many=False)
    period = PeriodSerializer()
    document_type = DocumentTypeSerializer(many=True)

    class Meta:
        model = Process
        fields = '__all__'

