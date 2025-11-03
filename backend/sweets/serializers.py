from rest_framework import serializers
from .models import Sweet


class SweetSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)
    category = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    quantity = serializers.IntegerField(required=True)

    def create(self, validated_data):
        sweet = Sweet(**validated_data)
        sweet.save()
        return sweet

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
