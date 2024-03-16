from rest_framework import serializers

from base.models import UserCheckpoint

from .user_logic import get_user


def get_checkpoint(user_id) -> UserCheckpoint:
    user_checkpoints = None
    if UserCheckpoint.objects.filter(user_id=user_id).exists():
        user_checkpoints = UserCheckpoint.objects.get(user_id=user_id)
        return CheckpointSerializer(user_checkpoints).data, 200

    return user_checkpoints, 404


def create_update_checkpoint(fields):
    serialized_checkpoint = None
    if get_checkpoint(fields['user_id'])[1] == 200:
        checkpoint = UserCheckpoint.objects.get(user_id=fields['user_id'])
        serialized_checkpoint = CheckpointSerializer(checkpoint, data=fields)
    else:
        if get_user(int(fields['user_id']))[1] == 200:
            serialized_checkpoint = CheckpointSerializer(data=fields)
        else:
            return serialized_checkpoint, 404
    if serialized_checkpoint.is_valid():
        serialized_checkpoint.save()
        return serialized_checkpoint.data, 201
    else:
        return serialized_checkpoint.errors, 400


class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCheckpoint
        fields = '__all__'
        fields = '__all__'
