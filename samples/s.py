from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    number = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.number = validated_data.get('number')
        instance.save()
        return instance