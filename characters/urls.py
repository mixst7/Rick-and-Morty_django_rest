from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, CharacterViewSet, EpisodeViewSet

router = DefaultRouter()
router.register('location', LocationViewSet)
router.register('character', CharacterViewSet)
router.register('episode', EpisodeViewSet)

urlpatterns = router.urls