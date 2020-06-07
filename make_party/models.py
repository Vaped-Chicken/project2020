from django.db import models

class Photo(models.Model):
    identificator = models.CharField('identity', max_length=150, blank=True)
    photo = models.ImageField('фото', upload_to = 'tmp1', blank=True)

    def __str__(self):
        return('i am photo')

class Changed_photo(models.Model):
    identificator = models.CharField('identity', max_length=150, blank=True)
    changed_photo = models.ImageField('changed фото', upload_to = 'tmp',blank=True)

    def __str__(self):
        return('i am changed photo')
