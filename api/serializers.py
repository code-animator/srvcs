from rest_framework import serializers

class resp_serialize(serializers.Serializer):
        status=serializers.IntegerField() #0=no prediction, #1=prediction made
        desc = serializers.CharField(max_length=256)
        pred = serializers.CharField(max_length=256)
        prediction=(status, desc, pred)
