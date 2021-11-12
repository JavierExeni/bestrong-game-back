from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from activities.models import Opcion


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = "__all__"


class OpcionViewset(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

    @action(detail=False, methods=['post'], url_path="lista-opciones",
            name="Traer todas las opciones según la actividad")
    def lista_opcion_by_actividad(self, request):
        if request.data['actividad']:
            queryset = Opcion.objects.filter(actividad=request.data['actividad'])
            serializer = OpcionSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según actividad")
