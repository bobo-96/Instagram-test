from rest_framework import serializers

from publication.models import Publications
from publication.serializers import PublicationsSerializer, PublicationImagesSerializer
from user.models import User, Favorites


class PublicationsForUserSerializer(serializers.ModelSerializer):
    post_images = PublicationImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Publications
        fields = ('id', 'owner', 'text', 'date', 'post_images')


class UserSerializer(serializers.ModelSerializer):
    post_owner = PublicationsForUserSerializer(many=True, read_only=True)
    favorite_publications =

    class Meta:
        model = User
        fields = ('phone', 'site', 'bio', 'username', 'first_name', 'last_name', 'email', 'post_owner')


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = '__all__'

