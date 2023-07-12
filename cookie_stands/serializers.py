from rest_framework import serializers
from .models import Cookie_stand


class Cookie_standserializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie_stand
        fields = "__all__"
