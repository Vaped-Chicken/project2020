import imageio
import os
import time
import pygifsicle
from django.conf import settings


def editorCore(array,token):
    b=time.time()
    # path = '/home/user/project/project2020/make_party/static/img/heads/'
    # list_of_img=os.listdir(path=path)
    #
    # image_folder = os.fsencode(path)
    #
    filenames = []
    #
    for file in array:
        filename = file
        filenames.append(file)
    #
    filenames.sort()


    images = list(map(lambda filename: imageio.imread(filename), filenames))
    print('images',images)
    DIR = os.path.join(settings.MEDIA_ROOT,token+'movie.gif')
    imageio.mimsave(DIR, images, duration = 1, fps = 1)

    print(DIR)
    pygifsicle.optimize(DIR)

    return (DIR.replace('/home/user/project/project2020/',''))
