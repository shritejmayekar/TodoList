from TodoList.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields =('__all__')
        exclude =('user',)
    def create(self, validated_data):        
        todo = Todo.objects.create(
            name=validated_data['name'],
            content=validated_data['content'],
            is_done=validated_data['is_done'],
            user= self.context['request'].user
        )
        return todo