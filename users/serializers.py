from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class RegistrationSerializer(serializers.ModelSerializers):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ['email','username','password','password2']
#         extra_kwargs = {
#                 'password': {'write_only': True}
#         }
