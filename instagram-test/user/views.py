from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from publication.models import Publications
from user.models import User, Favorites
from user.permissions import IsUserOwnerOrReadOnly
from user.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.prefetch_related('post_owner')
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly,)


class UserFavoritesView(APIView):

    def get(self, request, pk):
        publication = Publications.objects.get(id=pk)
        favorites = Favorites.objects.values_list('publication__text', flat=True).filter(publication=publication)
        return Response(favorites)


class FavoritesView(APIView):

    def get(self, request, pk):
        user = request.user
        publication = Publications.objects.get(id=pk)
        if Favorites.objects.filter(user=user, publication=publication).exists():
            Favorites.objects.filter(user=user, publication=publication).delete()
            return Response('Favorite Deleted', status=status.HTTP_201_CREATED)
        else:
            Favorites.objects.create(user=user, publication=publication)
            return Response('Favorite Saved', status=status.HTTP_200_OK)
