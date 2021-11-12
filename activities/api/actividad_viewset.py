from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from activities.models import Actividad


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class ActividadViewset(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    @action(detail=False, methods=['post'], url_path="lista-actividades",
            name="Traer todas las actividades según la lección")
    def lista_actividades_by_leccion(self, request):
        if request.data['leccion']:
            queryset = Actividad.objects.filter(leccion=request.data['leccion'])
            serializer = ActividadSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según leccion")
