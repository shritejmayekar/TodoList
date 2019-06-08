from TodoList.models import TodoNote,TodoList
from rest_framework import serializers


class TodoNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoNote
        # fields =('__all__')
        exclude =('user',)
    def create(self, validated_data):        
        note = TodoNote.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            is_done=validated_data['is_done'],
            user= self.context['request'].user
        )
        return note
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        # fields =('__all__')
        exclude =('user',)
    def create(self, validated_data):        
        todo = TodoList.objects.create(
            task=validated_data['task'],
            user= self.context['request'].user
        )
        return todo