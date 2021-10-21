from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from authentication.models import User, BodyInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "edad", "genero", "puntos", "bodyinfo"]


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
            return Response(UserSerializer(user, many=False).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
