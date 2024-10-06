import numpy as np
import pandas as pd
import requests

image = requests.get('https://avatars.mds.yandex.net/i?id=4f7586d49edaa427e07a8819562fc284_l-5248434-images-thumbs&n=13')
with open('1_image.png', 'wb') as f: # С помощью реквест мы спарсили картинку и сохранили ее у себя
    f.write(image.content)

import pandas

df = pd.read_csv('111_test_file.txt', delimiter=';') # Пандас помог нам работать с файлом, в том числе с разделителями в данном примере
print(df)

import matplotlib.pyplot as plt
import numpy


a = np.array([10, 20, 30, 40, 50, 60, 70, 80]) # данный код с помощью библиотек позволяет более просто работать с массивом чисел и совершать математические операции с ним
print(a)
print(a+10)
print(a-5)
print(a>35)

import matplotlib.pyplot
import numpy as np

phi = np.linspace(0, 2.*np.pi, 100) # здесь библиотеки помогают нам вызвать график синуса и косинуса
plt.plot(phi, np.sin(phi))
plt.plot(phi, np.cos(phi))


plt.show()

from PIL import Image

filename = 'Warrior Wallpaper.png' # а здесь мы берем любое изображение и редактируем его
with Image.open(filename) as img:
    img.load()
print(type(img))
print(img.size)

convert_img = img.transpose(Image.FLIP_TOP_BOTTOM) # например перевернем его низм к верху
convert_img.save('1_Warrior Wallpaper.png')

rotate_img = img.rotate(45) # или повернем на 45 градусов
rotate_img.save('2_Warrior Wallpaper.png')

rotate_img = img.rotate(-45) # можно сделать и - 45 градусов
rotate_img.save('3_Warrior Wallpaper.png')

rotate_img = img.rotate(90) # или перевернуть на 90 
rotate_img.save('4_Warrior Wallpaper.png')



