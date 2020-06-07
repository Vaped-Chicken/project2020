import random
import requests
import os
import time
from PIL import Image
import socket
import socks


ip='3.17.56.86' # change your proxy's ip
port = 9956 # change your proxy's port
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket

# list_of_img=os.listdir(path="/home/user/project/project2020/make_party/static/img/outputs")
number_of_sticker = len(list_of_img)
sticker_set_name="pack_"+str(random.randint(10000,99999))+"_by_VapedChickenStuff_bot"
emojis = [
'\U0001F601',
'\U0001F602',
'\U0001F603',
'\U0001F604',
'\U0001F605',]

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
    payload = {'user_id': user_id, 'text': text}
    response = requests.post(url, files=up, data=payload)

def tg_create_pack(user_id,name):
    url="https://api.telegram.org/bot1061196327:AAHsJBoIi_Yw4uC1EsHWRffMIE3GPJUr2xY/createNewStickerSet"
    payload = {'user_id': user_id, 'name': name, 'title': 'VapedChickenStuff_bot', 'emojis': '\U0001F609'}
    up = {'png_sticker':('logo.png', open('/home/user/project/project2020/make_party/logo.png', 'rb'), "multipart/form-data")}
    response = requests.post(url, files=up, data=payload)

def tg_add_stiekr_to_pack(user_id,name,emoj,stiker_name):
    url="https://api.telegram.org/bot1061196327:AAHsJBoIi_Yw4uC1EsHWRffMIE3GPJUr2xY/addStickerToSet"
    payload = {'user_id': user_id, 'name': name, 'title': 'VapedChickenStuff_bot', 'emojis': emoj}
    up = {'png_sticker':('/home/user/project/project2020/make_party/static/img/outputs/'+stiker_name, open('/home/user/project/project2020/make_party/static/img/outputs/'+stiker_name, 'rb'), "multipart/form-data")}
    response = requests.post(url, files=up, data=payload)

def stikers_maker(user_id,list_of_img):
    print(list_with_paths)
    tg_create_pack(user_id,sticker_set_name)
    for stiker in range(0,number_of_sticker):
        resize_image(input_image_path='/home/user/project/project2020/make_party/static/img/outputs/'+list_of_img[stiker],
                     output_image_path='/home/user/project/project2020/make_party/static/img/outputs/'+list_of_img[stiker],
                     size=(512, 512))
        tg_add_stiekr_to_pack(user_id,sticker_set_name,emojis[stiker],list_of_img[stiker])
    return sticker_set_name
