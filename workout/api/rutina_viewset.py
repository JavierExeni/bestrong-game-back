from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from workout.models import Rutina


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = "__all__"


class RutinaViewset(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

    @action(detail=False, methods=['post'], url_path="lista-rutinas",
            name="Traer todas las rutinas según el nivel")
    def lista_rutinas_by_nivel(self, request):
        if request.data['nivel']:
            queryset = Rutina.objects.filter(id=request.data['nivel'])
            serializer = RutinaSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según leccion")

    @action(detail=False, methods=['post'], url_path="update-rutina",
            name="Update rutina sacando user")
    def update_rutina_user(self, request):
        if request.data['rutina'] and request.data['user'] and request.data['nivel']:
            Rutina.objects.filter(id=request.data['rutina']).first().user.remove(request.data['user'])
            Rutina.objects.filter(nivel_id=int(request.data['nivel']+1)).first().user.add(request.data['user'])
            queryset = Rutina.objects.filter(nivel_id=int(request.data['nivel']+1)).first()
            serializer = RutinaSerializer(queryset, many=False)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según rutina")
