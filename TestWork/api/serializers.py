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


class GateSerializer(serializers.ModelSerializer):
    num_chekpoint = serializers.CharField()

    class Meta:
        model = models.Gate
        fields = ('num_chekpoint',)

    def update(self, instance, validated_data):
        instance.num_chekpoint = validated_data.get('num_chekpoint', instance.num_chekpoint)
        instance.save()
        return instance


class LogVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LogVisit
        fields = ('user', 'time_detection', 'permit_id', 'status', 'num_checkpoint',)
