from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from activities.models import Leccion


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = "__all__"


class LeccionViewset(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer

    @action(detail=False, methods=['post'], url_path="lista-lecciones",
            name="Traer todas las lecciones según el nivel")
    def lista_leccion_by_nivel(self, request):
        if request.data['nivel']:
            queryset = Leccion.objects.filter(nivel=request.data['nivel'])
            serializer = LeccionSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según nivel")
