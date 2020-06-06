from django.shortcuts import render
from django.http import HttpResponse
from . import faceswap
from PIL import Image
import os
# from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
from .models import Photo
from django.conf import settings
import json


api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM'

def index(request):

    return render(
        request,
        'index.html',
        # { },
    )




def change_photo(request):

    files = request.FILES
    print(files)

    # photo = (files['image'])

    filename = "photo.jpg"
    # file_obj = request.data['file']
    # print(default_storage)
    # with default_storage.open('tmp/'+filename, 'wb+') as destination:
    #     for chunk in photo.chunks():
    #         destination.write(chunk)
    #         print(destination)

    # head = Image.open(r'/home/user/spend/head5.jpg')
    head = '/home/user/spend/face4.jpg'
    # face = default_storage.open('tmp/'+filename, 'wb+')

    file = request.FILES['image']
    print(file.read())
    file.name ='kek.jpg'
    obj, created = Photo.objects.get_or_create(photo = file
                                            )
    if created:
        obj.save()
    else:
        root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
        os.remove(root)
        obj.photo = file
        obj.save()

    # path = cv2.imwrite('/home/user/project/project2020/make_party/static/img/outputs/output.jpg', file)
    path = obj.photo.url
    print('path',path)
    root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
    print('root', root)


    final = faceswap.core(head,root)
    # cv2.imwrite('/home/user/project/project2020/make_party/static/img/outputs/output.jpg', final)
    # jpeg = open('/home/user/project/project2020/make_party/static/img/outputs/output.jpg','r')
    # print(jpeg)

    count_list = {
        'url' : 'static/img/outputs/output.jpg',
    }
    count_list = json.dumps(count_list,sort_keys = True, indent = 4)


    return HttpResponse(count_list)
