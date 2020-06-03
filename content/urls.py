from .views import MatchViewSet, ContributeViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register('match', MatchViewSet)
router.register('contribute', ContributeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
