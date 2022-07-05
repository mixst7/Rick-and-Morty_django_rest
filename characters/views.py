from rest_framework.viewsets import ModelViewSet
from .models import Location, Character, Episode
from .serializers import LocationSerializers, CharacterSerializers, EpisodeSerializers


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializers

class EpisodeViewSet(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializers