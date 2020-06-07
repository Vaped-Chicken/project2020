import random
import requests
import os
from PIL import Image
import socket
import socks
import json



ip='3.17.56.86' # change your proxy's ip
port = 9956 # change your proxy's port
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket

# list_of_img=os.listdir(path="/home/user/project/project2020/make_party/static/img/outputs")
# number_of_sticker = len(list_of_img)
sticker_set_name="pack_"+str(random.randint(10000,99999))+"_by_VapedChickenStuff_bot"
emojis = [
'\U0001F601',
'\U0001F602',
'\U0001F603',
'\U0001F604',
'\U0001F605',
'\U0001F648',
'\U0001F649',
'\U0001F64A',
'\U0001F64B',
'\U0001F64C',
'\U0001F64D',
'\U0001F64E',]


def get_crop(file):
    face=data[0]
    box=face['bbox']
    first_corner=box[0]
    second_corner=box[1]

    img = Image.open(file)
    (width, height) = img.size
    #
    cropped = img.crop((first_corner[0], first_corner[1], second_corner[0], second_corner[1]))
    cropped.save('/home/user/project/project2020/make_party/cpored/done.jpg')


def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    resized_image.save(output_image_path)


def send_message(user_id):
    text="Ваш стикер пак"+sticker_set_name+" доступен у официального бота телеграмм @Stickers.\nСтикер пак будет в общем доступе в течении часа.\nУ официального бота мы можете модерировать стикер пак.\nХорошего дня:)"
    url="https://api.telegram.org/bot1061196327:AAHsJBoIi_Yw4uC1EsHWRffMIE3GPJUr2xY/sendMessage"
    payload = {'chat_id': user_id, 'text': text}
    response = requests.post(url,  data=payload)
    # print("send ",response.text)

def tg_create_pack(user_id,name):
    url="https://api.telegram.org/bot1061196327:AAHsJBoIi_Yw4uC1EsHWRffMIE3GPJUr2xY/createNewStickerSet"
    payload = {'user_id': 249987725, 'name': name, 'title': 'VapedChickenStuff_bot', 'emojis': '\U0001F609'}
    up = {'png_sticker':('logo.png', open('/home/user/project/project2020/make_party/logo.png', 'rb'), "multipart/form-data")}
    response = requests.post(url, files=up, data=payload)
    # print(response.text)
    # print(payload)

def tg_add_stiekr_to_pack(user_id,name,emoj,stiker_name):
    url="https://api.telegram.org/bot1061196327:AAHsJBoIi_Yw4uC1EsHWRffMIE3GPJUr2xY/addStickerToSet"
    payload = {'user_id': user_id, 'name': name, 'title': 'VapedChickenStuff_bot', 'emojis': emoj}
    up = {'png_sticker':(stiker_name, open(stiker_name, 'rb'), "multipart/form-data")}
    response = requests.post(url, files=up, data=payload)
    print(response.text)

def stikers_maker(user_id,list_of_img,token):
    number_of_sticker = len(list_of_img)
    print(sticker_set_name)
    tg_create_pack(user_id,sticker_set_name)
    for stiker in range(0,number_of_sticker-1):
        resize_image(input_image_path=list_of_img[stiker],
                     output_image_path='/home/user/project/project2020/make_party/cpored/'+str(stiker)+str(token)+'.png',
                     size=(512, 512))
        sticker_name_png ='/home/user/project/project2020/make_party/cpored/'+str(stiker)+str(token)+'.png'
        tg_add_stiekr_to_pack(user_id,sticker_set_name,emojis[stiker],sticker_name_png)
    send_message(user_id)
    return sticker_set_name
