from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import *
from .widgets import *
from django import forms
from django.contrib import messages
from django.shortcuts import  redirect
from django.utils.encoding import smart_str


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 5
    fields = ['image_tag',]

class GalleryForm(forms.ModelForm):
    class Meta:
       model = Gallery
       widgets = {'image': MultiFileInput}
       fields = '__all__'

class PhotoAdmin(admin.ModelAdmin):
   admin_thumbnail = AdminThumbnail(image_field='photo')
   list_filter = ['gallery_id']
   list_per_page = 50
   fields = ('image_tag', 'gallery')
   readonly_fields = ('image_tag',)
   class Meta:
      model = Photo

admin.site.register(Photo, PhotoAdmin)

class GalleryAdmin(admin.ModelAdmin):
   list_display = ('name', 'date', 'private', 'password', 'countPhoto')
   inlines = [PhotoInline]
   list_filter = ['private']
   form = GalleryForm
   date_hierarchy = 'date'
   ordering = 'date', 'name'

   def save_model(self, request, obj, form, change):

       super(GalleryAdmin, self).save_model(request, obj, form, change)
       # obj.save()

       for afile in request.FILES.getlist('photos_multiple'):
           obj.images.create(photo=afile)

admin.site.register(Gallery, GalleryAdmin)
