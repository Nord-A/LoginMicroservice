from django.contrib.auth.signals import user_logged_in
from rest_framework.authtoken.models import Token
from logpipe import Producer
import uuid
from rest_framework import serializers
from django.db import models

class TokenUser(models.Model):
    tokenid = models.CharField(max_length=40)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    
class TokenUserSerializer(serializers.ModelSerializer):
    MESSAGE_TYPE = 'tokenuser'
    VERSION = 1
    KEY_FIELD = 'uuid'

    class Meta:
        model = TokenUser
        fields = ['tokenid', 'uuid']


def send_kafka_token(sender, user, request, **kwargs):
    token = str(Token.objects.get(user_id=user.id))
    test = TokenUser.objects.create(tokenid=token)
    producer = Producer('login2', TokenUserSerializer)
    producer.send(test)

user_logged_in.connect(send_kafka_token)
