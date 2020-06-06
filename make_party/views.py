from django.shortcuts import render
from django.http import HttpResponse
from . import faceswap
# from PIL import Image
import os
# from django.utils import timezone
# from django.core.files.storage import default_storage
import cv2
from .models import Photo
from django.conf import settings
import json
import base64
from django.core.files import File
from django.core.files.base import ContentFile


api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM'

def index(request):

    return render(
        request,
        'index.html',
        # { },
    )




def change_photo(request):


    file = request.POST['image']
    encodedPhoto = file.replace('data:image/jpeg;base64,','')

    decodedPhoto = base64.urlsafe_b64decode(encodedPhoto)
    finalPhoto = ContentFile(decodedPhoto, name='kek.jpg')

    obj, created = Photo.objects.get_or_create(photo = finalPhoto)
    if created:
    # если не было записи и она создалась тут можно что то еще добавить
        obj.save()
    else:
        root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
        os.remove(root)
        obj.photo = finalPhoto
        obj.save()


    head = '/home/user/project/project2020/make_party/static/img/heads/77-minimy.jpg'
    root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
    final = faceswap.core(head,root)




    # file = request.FILES['image']
    # print(file.read())
    # file.name ='kek.jpg'
    # obj, created = Photo.objects.get_or_create(photo = file
    #                                         )
    # if created:
    #     obj.save()
    # else:
    #     root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
    #     os.remove(root)
    #     obj.photo = file
    #     obj.save()


    #
    #
    # # path = cv2.imwrite('/home/user/project/project2020/make_party/static/img/outputs/output.jpg', file)
    # path = obj.photo.url
    # print('path',path)
    # print('root', root)
    #
    #
    # # cv2.imwrite('/home/user/project/project2020/make_party/static/img/outputs/output.jpg', final)
    # # jpeg = open('/home/user/project/project2020/make_party/static/img/outputs/output.jpg','r')
    # # print(jpeg)



    count_list = {
        'url' : 'static/img/outputs/output.jpg',
    }
    count_list = json.dumps(count_list,sort_keys = True, indent = 4)


    return HttpResponse(count_list)
