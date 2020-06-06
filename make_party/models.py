from django.db import models

class Photo(models.Model):
    photo = models.ImageField('фото', upload_to = 'tmp',blank=True)

    def __str__(self):
        return('i am photo')

class Changed_photo(models.Model):
    changed_photo = models.ImageField('changed фото', upload_to = 'tmp',blank=True)

    def __str__(self):
        return('i am changed photo')
