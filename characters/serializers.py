from rest_framework import serializers
from .models import Location, Character, Episode

class LocationSerializers(serializers.ModelSerializer):
    birth_location = serializers.StringRelatedField(many=True, read_only=True)
    current_location = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ('id', 'title', 'universe', 'desc', 'image', 'created', 'birth_location', 'current_location')

class CharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'status', 'desc', 'gender', 'race', 'birth_location', 'current_location')

class EpisodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'title', 'number_episode', 'desc', 'characters')
