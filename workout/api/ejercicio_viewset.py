from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from workout.models import Ejercicio


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = "__all__"


class EjercicioViewset(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

    @action(detail=False, methods=['post'], url_path="lista-ejercicios",
            name="Traer todas los ejercicios según la rutina")
    def lista_ejercicios_by_rutina(self, request):
        if request.data['rutina']:
            queryset = Ejercicio.objects.filter(rutina=request.data['rutina'])
            serializer = EjercicioSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según leccion")
