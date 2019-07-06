from main.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_superuser',)
        extra_kwargs = {'password': {'write_only': True, 'required': True,
                        'help_text': 'Leave empty if no change needed',
                        'style': {'input_type': 'password', 'placeholder': 'Password'}
        }}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


