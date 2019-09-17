from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe

class Gallery(models.Model):
    name = models.CharField(max_length=30, default=" ")
    date = models.DateField()
    private = models.BooleanField(default=False)
    password = models.CharField(max_length=50)

    def countPhoto(self):
        return len(Photo.objects.filter(gallery_id=self.id))

    class Meta:
        verbose_name = "Фотосьемка"
        verbose_name_plural = "Фотосьёмки"

    def __str__(self):
         return self.name


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to='photos')
    photoThumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})

    def image_tag(self):
        return mark_safe('<img src="/media/%s"/>' % (self.photoThumbnail))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return str(self.id)
