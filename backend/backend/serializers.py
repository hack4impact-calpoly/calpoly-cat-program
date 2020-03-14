from django.contrib.auth.models import User, Group
from directory.models import Client
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Serializer for Client Model, allows for adding Clients to database
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'birthday', 'location']


# Serializer for adding User to Database this will be used for admins/john. We need to use User model for authentication
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
