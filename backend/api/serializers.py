from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
