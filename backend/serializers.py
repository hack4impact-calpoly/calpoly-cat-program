from django.contrib.auth.models import User, Group
from rest_framework import fields, serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from directory.models import Cat
from directory.models import PERSONALITY
from directory.models import Document
from directory.models import Photo
from directory.models import Event

class CatSerializer(serializers.HyperlinkedModelSerializer):
    personality = fields.MultipleChoiceField(choices=PERSONALITY)
    class Meta:
        model = Cat
        fields = [
            'name', 'gender', 'age', 'birthday', 'description', 'breed', 'itype', 'status',
            'arrival_date', 'arrival_details', 'medical_history', 'vaccinations',
            'is_microchipped', 'flea_control_date', 'deworming_date', 'fiv_felv_date',
            'special_needs', 'personality', 'more_personality', 'comments',
            'personal_exp'
        ]

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['cat_id', 'document', 'description', 'uploaded_at', 'hidden']

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['cat_id', 'photo', 'description', 'uploaded_at', 'hidden']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    # add cat name to API read for easier access
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Event
        fields = ['cat_id', 'name', 'event_type', 'title', 'date', 'time', 'notes']

# Serializer for adding User to Database this will be used for admins. We need to use User model for authentication
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
