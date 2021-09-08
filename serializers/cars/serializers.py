from rest_framework import serializers
from . import models


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return models.Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    """ModelSerializer"""
    # class Meta:
    #     model = models.Brand
    #     fields = '__all__'


class MadelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    brand_id = serializers.IntegerField()
    position = serializers.IntegerField()

    def create(self, validated_data):
        return models.Madel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.brand_id = validated_data.get('brand_id', instance.brand_id)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance

    """ModelSerializer"""
    class Meta:
        model = models.Madel
        fields = '__all__'
        