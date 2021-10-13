from rest_framework import serializers, viewsets

from authentication.models import BodyInfo


class BodyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyInfo
        fields = "__all__"


class BodyInfoViewset(viewsets.ModelViewSet):
    queryset = BodyInfo.objects.all()
    serializer_class = BodyInfoSerializer
