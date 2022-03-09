# TODO: опишите сериализаторы
from rest_framework import serializers

from measurements.models import Project, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['value', 'created_at', 'updated_at','project_id']


class ProjectDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'measurements']