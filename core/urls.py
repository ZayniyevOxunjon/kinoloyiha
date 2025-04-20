from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CountryViewSet, GenreViewSet, FilmViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'films', FilmViewSet, basename='films')

urlpatterns = [
path('', include(router.urls)),
]

