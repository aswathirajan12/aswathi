from rest_framework import serializers
from.models import student

# class sample(serializers.Serializer):
#     roll=serializers.IntegerField()
#     name=serializers.CharField(max_length=50)
#     age=serializers.IntegerField()

class sample(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'