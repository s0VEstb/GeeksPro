from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']


class TaskValiditySerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=50)
    description = serializers.CharField(min_length=1, max_length=150)
    completed = serializers.BooleanField(default=False)

    def validate_title(self, title):
        if Task.objects.filter(title=title).exists():
            raise serializers.ValidationError("Title already exists")
        return title


