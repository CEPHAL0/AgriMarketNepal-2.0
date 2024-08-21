from rest_framework.serializers import ModelSerializer
from .models import Province


class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        fields = ["name"]

    def create(self, **validated_data):
        """
        Create and return a new `Province` instance, given the validated data.
        """
        return Province.objects.create(**validated_data)

    def update(self, instance, **validated_data):
        """
        Update and return an existing `Province` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
