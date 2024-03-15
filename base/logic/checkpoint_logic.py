from rest_framework import serializers

from base.models import UserCheckpoint


def get_checkpoint(user_id) -> UserCheckpoint:
    user_checkpoints = None
    if UserCheckpoint.objects.filter(user_id=user_id).exists():
        user_checkpoints = UserCheckpoint.objects.get(user_id=user_id)
        return CheckpointSerializer(user_checkpoints).data


    return user_checkpoints

class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCheckpoint
        fields = '__all__'

