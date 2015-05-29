from django.forms import widgets
from rest_framework import serializers
from api.models import Idea, Note


class IdeaSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Idea
        fields = ('name', 'description', 'notes')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ('body')
