from rest_framework import serializers, viewsets

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    edad = serializers.IntegerField(required=True)
    genero = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = "__all__"


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
