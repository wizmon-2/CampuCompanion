from rest_framework import serializers
from .models import Todo, Groups

class CreateTodoSerializer(serializers.Serializer):
    gid = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    due_date = serializers.DateField()


    def create(self, validated_data):
        td = Todo(title=validated_data['title'], description=validated_data['description'], due_date=validated_data['due_date'])
        group = Groups.objects.filter(id=validated_data['gid'])
        if group.exists():
            td.group = group[0]
        else:
            raise serializers.ValidationError({"detail": "Group does not exist"})
        td.save()

        return td