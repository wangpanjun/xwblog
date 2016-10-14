from rest_framework import serializers
from labels.models import LabelModel


class LabelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LabelModel
        fields = ('id', 'from_user', 'to_user', 'label')
