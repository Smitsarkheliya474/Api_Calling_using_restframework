from rest_framework import serializers
from .models import Employee

class EmplSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    salary = serializers.CharField(max_length=10)
    contact = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=20)
    
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance