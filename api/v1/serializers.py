from django.forms import widgets
from rest_framework import serializers
from api.models import Idea, Note


class IdeaSerializer(serializers.ModelSerializer):
    elevator_pitch = serializers.CharField(source='description')

    class Meta:
        model = Idea
        fields = ('name', 'elevator_pitch')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ('body',)
