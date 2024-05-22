from PIL import Image, ImageFilter
import os

def pic1():
    image = Image.open('pic.jpg')
    image.show()
    print("Размер изображения:", image.size)

    print("Формат изображения:", image.format)

    print("Цветовая модель изображения:", image.mode)    #какой rgb

def pic2():
    image = Image.open('pic.jpg')
    image.save("pic0.jpg")  #сохранение

    res_img = image.resize((245, 245))
    res_img.save("pic4.jpg")  #сохраняет с измененным размером

    res = image.transpose(Image.FLIP_TOP_BOTTOM)
    res.save("pic2.jpg")      #отзеркаливает горизонтально

    res_i = image.transpose(Image.FLIP_LEFT_RIGHT)
    res_i.save("pic1.jpg")    #отзеркаливает вертикально
    print("Обработка изображений завершена.")

def pic3():
    nach = 'E:/дз/алгоретмизация/2 сем/7 лаба'
    obrabot = 'E:/дз/алгоретмизация/2 сем/7 лаба/pac'
    if not os.path.exists(obrabot):
        os.makedirs(obrabot)  #обработка в директр

    imag = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for image_name in imag:
        image = Image.open(os.path.join(nach, image_name))     #обЪединяет в одну строку

        image_filtered = image.filter(ImageFilter.CONTOUR)     # обработ конур

        new_image_name = 'filtered_' + image_name
        image_filtered.save(os.path.join(obrabot, new_image_name))    # сохраняет обработ фото  вновую папку обработ

    print("Обработка изображений завершена.")

def pic4():
    pyt = 'E:/дз/алгоретмизация/2 сем'
    water = 'E:/дз/алгоретмизация/2 сем/7 лаба/watermark.png'
    obrabotan = 'E:дз/алгоретмизация/2 сем/7 лаба/pac'

    if not os.path.exists(obrabotan):
        os.makedirs(obrabotan)       #создает папку если ее нет

    image_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for image_name in image_names:
        image = Image.open(os.path.join(obrabotan, image_name))

        watermark = Image.open(water)                        #открывает
        size = (100, 100)
        watermark = watermark.resize(size)                   # меняет размер марки

        watermark_width, watermark_height = watermark.size   #вычисляет размеры фото и марки

        image_width, image_height = image.size

        wtyt = (image_width - watermark_width, image_height - watermark_height)   #доб знак

        image.paste(watermark, wtyt, watermark)

        new_image_name = 'watermarked_' + image_name
        image.save(os.path.join(obrabotan, new_image_name))
    print("Добавление водяного знака завершено.")

while True:
    print('1. показ картинки')
    print('2. транспортировать')
    print('3. 5 фото')
    print('4. водяной знак')
    print('5. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        pic1()
    elif a == 2:
        pic2()
    elif a == 3:
        pic3()
    elif a == 4:
        pic4()
    elif a == 5:
        break
    else:
        print('Неверное действие')
pic1()
