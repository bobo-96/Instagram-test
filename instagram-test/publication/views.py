from django.db.models import F
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from publication.models import Publications
from publication.serializers import PublicationsSerializer


class PublicationsView(ModelViewSet):
    serializer_class = PublicationsSerializer
    queryset = Publications.objects.prefetch_related('post_images').annotate(
        owner_nick_name=F('owner__username'),
        owner_avatar=F('owner__avatar')
    ).order_by('-date')
    lookup_field = 'pk'

    def get_object(self):
        return Publications.objects.prefetch_related('post_images').annotate(
            owner_nick_name=F('owner__username'),
            owner_avatar=F('owner__avatar')
        ).get(id=self.kwargs['pk'])
