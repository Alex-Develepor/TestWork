from rest_framework import serializers

from . import models


class UserOSSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    status = serializers.BooleanField()
    permit = serializers.SerializerMethodField()

    class Meta:
        model = models.UserOS
        fields = ('login', 'time_detection', 'status', 'permit')

    def get_permit(self, obj):
        return obj.login + str(obj.time_detection)

    def update(self, instance, validated_data):
        instance.login = validated_data.get('login', instance.login)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
