from rest_framework import serializers, viewsets

from authentication.models import Logro


class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro
        fields = "__all__"


class LogroViewset(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer
