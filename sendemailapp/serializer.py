from rest_framework import serializers
from .models import SendMail


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = SendMail
        fields = ('id', 'receiver', 'subject', 'body', 'namereceiver')
