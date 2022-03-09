from rest_framework.viewsets import ModelViewSet

from measurements.models import Measurement, Project
from measurements.serializers import MeasurementSerializer, ProjectDetailSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
