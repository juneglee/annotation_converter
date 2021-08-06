from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause'
                  ,'votes_to_skip','created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

# class ShapeSerializer(serializers.Serializer):
#     type = serializers.ChoiceField(choices=models.ShapeType.choices())
#     occluded = serializers.BooleanField()
#     z_order = serializers.IntegerField(default=0)
#     points = serializers.ListField(
#         child=serializers.FloatField(),
#         allow_empty=False,
#     )