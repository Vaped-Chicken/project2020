from django.shortcuts import render
from django.http import HttpResponse
from . import faceswap
# from PIL import Image
import os
# from django.utils import timezone
# from django.core.files.storage import default_storage
import cv2
from .models import Photo,Changed_photo
from django.conf import settings
import json
import base64
from django.core.files import File
from django.core.files.base import ContentFile
from . import skiterbot
import random

api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM'

def index(request):

    return render(
        request,
        'index.html',
        # { },
    )




def change_photo(request):
    print('nachal')
    token = request.POST['csrf']
    file = request.POST['image']
    encodedPhoto = file.replace('data:image/jpeg;base64,','')

    decodedPhoto = base64.urlsafe_b64decode(encodedPhoto)
    finalPhoto = ContentFile(decodedPhoto, name='kek.jpg')

    obj, created = Photo.objects.get_or_create(photo = finalPhoto)
    if created:
    # если не было записи и она создалась тут можно что то еще добавить
        obj.identificator = token
        obj.save()
    else:
        root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
        print(root)
        os.remove(root)
        obj.photo = finalPhoto
        obj.identificator = token
        obj.save()

    list_of_img=os.listdir(path="/home/user/project/project2020/make_party/static/img/heads/")
    # print(list_of_img)
    # head = '/home/user/project/project2020/make_party/static/img/heads/'+list_of_img[random.randint(0,len(list_of_img)-1)]


    array_photo =[]
    print('start array_photo',array_photo)
    a=0
    for index in list_of_img:
        # print(a)
        head = '/home/user/project/project2020/make_party/static/img/heads/'+index
        # print('head_path',head)
        root = os.path.join(settings.MEDIA_ROOT,obj.photo.name)
        # print('root_path',root)
        final = faceswap.core(head,root)

        # ch_file = str(open('/home/user/project/project2020/media/output.jpg','rb').read()).replace('data:image/jpeg;base64,','')
        # decodedPhoto = base64.urlsafe_b64decode(ch_file)
        # print(decodedPhoto)
        chPhoto = open('/home/user/project/project2020/media/output.jpg','rb')
        # print(chPhoto.name)
        photo_name = 'final'+obj.photo.name.replace('tmp1/','').replace('.jpg','')+str(a)+'.jpg'
        final_ch_file = File(chPhoto,name = photo_name)
        print('final',final_ch_file)
        Changed_photo.objects.create(identificator=token,
                                     changed_photo=final_ch_file)
        a=a+1
        array_photo.append('/home/user/project/project2020/media/tmp/'+photo_name)
        print('array_photo',array_photo)
        # print(a)
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

    print(array_photo)
    count_list = {
        'url' : 'static/img/outputs/output.jpg',
    }
    count_list = json.dumps(count_list,sort_keys = True, indent = 4)


    return HttpResponse(count_list)

def create_stickerpack(request):

    token = request.POST['csrf']
    userid = request.POST['userid']
    list = Changed_photo.objects.filter(identificator=token)
    final_list_of_img = []
    for index in list:
        print(index.changed_photo.path)
        final_list_of_img.append(index.changed_photo)
    # print(final_list_of_img)
    # stickerpack = {
    #     'name' : skiterbot.stikers_maker(userid)#,final_list_of_img),
    # }
    # stickerpack = json.dumps(stickerpack,sort_keys = True, indent = 4)

    return HttpResponse('xhtoto')
    # return HttpResponse(stickerpack)
