from rest_framework import serializers, viewsets

from activities.models import Leccion


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = "__all__"


class LeccionViewset(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
