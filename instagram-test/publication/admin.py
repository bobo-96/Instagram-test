from django.contrib import admin
from publication.models import Publications, PublicationImages


class PublicationImagesInline(admin.TabularInline):
    model = PublicationImages
    extra = 0


class PublicationsAdmin(admin.ModelAdmin):
    inlines = [PublicationImagesInline]
    readonly_fields = ('date',)


admin.site.register(Publications, PublicationsAdmin)
