import numpy as np
import pandas as pd
import requests

image = requests.get('https://avatars.mds.yandex.net/i?id=4f7586d49edaa427e07a8819562fc284_l-5248434-images-thumbs&n=13')
with open('1_image.png', 'wb') as f:
    f.write(image.content)

import pandas

df = pd.read_csv('111_test_file.txt', delimiter=';')
print(df)

import matplotlib.pyplot as plt
import numpy


a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(a)
print(a+10)
print(a-5)
print(a>35)

import matplotlib.pyplot
import numpy as np

phi = np.linspace(0, 2.*np.pi, 100)
plt.plot(phi, np.sin(phi))
plt.plot(phi, np.cos(phi))


plt.show()

from PIL import Image

filename = 'Warrior Wallpaper.png'
with Image.open(filename) as img:
    img.load()
print(type(img))
print(img.size)

convert_img = img.transpose(Image.FLIP_TOP_BOTTOM)
convert_img.save('1_Warrior Wallpaper.png')

rotate_img = img.rotate(45)
rotate_img.save('2_Warrior Wallpaper.png')

rotate_img = img.rotate(-45)
rotate_img.save('3_Warrior Wallpaper.png')

rotate_img = img.rotate(90)
rotate_img.save('4_Warrior Wallpaper.png')



