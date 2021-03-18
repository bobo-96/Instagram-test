from django.conf import settings
from django.db import models


class Publications(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'post_owner')
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        # ordering = ('-date', )

    def __str__(self):
        return self.text


class PublicationImages(models.Model):
    publication = models.ForeignKey('publication.Publications', models.CASCADE, 'post_images')
    image = models.FileField('Фото', upload_to='post_images')


