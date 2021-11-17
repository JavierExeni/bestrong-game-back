from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.api import BodyInfoSerializer, LogroSerializer
from authentication.models import User
from store.api import ProductoSerializer
from workout.api import RutinaSerializer
from workout.models import Rutina


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "edad", "genero", "puntos",
                  "bodyinfo", "producto", "logro"]


class UserResponseSerializer(serializers.ModelSerializer):
    bodyinfo = BodyInfoSerializer(many=False, read_only=True)
    producto = ProductoSerializer(many=True, read_only=True)
    logro = LogroSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "edad", "genero", "puntos", "bodyinfo",
                  "producto", "logro"]


class UserRegisterSerializer(serializers.Serializer):
    edad = serializers.IntegerField(required=True)
    genero = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data, context={'request': self.request})
        if serializer.is_valid():
            user = User()
            user.first_name = serializer.data['first_name']
            user.last_name = serializer.data['last_name']
            user.email = serializer.data['email']
            user.username = serializer.initial_data['username']
            user.genero = serializer.data['genero']
            user.edad = serializer.data['edad']
            user.set_password(serializer.initial_data['password'])
            user.puntos = serializer.data['puntos'] if 'puntos' in serializer.data else 0

            user.save()
            return Response(UserResponseSerializer(user, many=False).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserResponseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserResponseSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(UserResponseSerializer(instance, many=False).data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @action(detail=False, methods=['post'], url_path="get-rutina",
            name="Obtener rutina de user")
    def get_rutina_user(self, request):
        if request.data['user']:
            queryset = Rutina.objects.filter(user=request.data['user']).first()
            serializer = RutinaSerializer(queryset, many=False)
            return Response(serializer.data)
        else:
            return Response("No se encontraron según rutina")
