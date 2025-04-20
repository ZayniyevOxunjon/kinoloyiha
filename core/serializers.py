from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Genre, Country, Film, Rating, Comment, Favorite
from users.serializers import UserSerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Film
        fields = [
            'id', 'title', 'body', 'image', 'video_url', 'year', 'age_limit',
            'created_at', 'updated_at', 'category', 'genres', 'country', 'download_number'
        ]

class FilmCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'film', 'user', 'value']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'film', 'user', 'text', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'film', 'is_like']