from rest_framework import serializers

from publication.models import Publications, PublicationImages
from user.models import User


class PublicationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicationImages
        fields = ('id', 'image')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')


class PublicationsSerializer(serializers.ModelSerializer):
    post_images = PublicationImagesSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Publications
        fields = ('id', 'owner', 'text', 'date', 'post_images')

    def create(self, validated_data):
        user = self.context.get('request').user
        publication = Publications.objects.create(owner=user, **validated_data)
        images = self.context.get('request').data.getlist('post_images')
        images_list = [PublicationImages(image=item, publication=publication) for item in images]
        PublicationImages.objects.bulk_create(images_list)
        return publication

    def update(self, instance, validated_data):
        for attr, value, in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        images = self.context.get('request').data.getlist('post_images')
        if images:
            PublicationImages.objects.filter(publication=instance).delete()
            images_list = [PublicationImages(image=item, publication=instance) for item in images]
            PublicationImages.objects.bulk_create(images_list)
        return instance
