from rest_framework.serializers import ModelSerializer
from api.models import Tarefa

from django.contrib.auth import get_user_model
from rest_framework import serializers

class TarefaSerializer(ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Tarefa
        fields = '__all__'
        
User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user