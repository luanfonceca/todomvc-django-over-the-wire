
from rest_framework import serializers

from todos.models import ToDo


class ToggleToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('is_completed',)
