from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'date_joined', 'last_login')

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.username = validated_data.get('username')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, value):
        user = User.objects.filter(username=value)
        if len(user) != 0:
            raise serializers.ValidationError("Username already exists")
        else:
            return value
        
