# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt


def get_right(height_result, key_height):
    # срез справа от максимальной высоты
    height_result_right = height_result[0:key_height]

    result_second_height = 0

    # перебираем врпаво
    for enum, item in enumerate(height_result_right):
        if item > height_result_right[enum]:
            result_second_height = item
        else:
            result_second_height = height_result_right[enum]

    return result_second_height


def get_left(height_result, key_height):
    # срез влево от максимальной высоты
    height_result_left = height_result[key_height:]

    result_second_height = 0

    # перебираем влево
    for enum, item in enumerate(height_result_left):
        if item > height_result_left[enum]:
            result_second_height = item
        else:
            result_second_height = height_result_left[enum]

    return result_second_height


# отображение графика координат для теста
def show_gr(x, y):
    plt.xlabel("X")
    plt.ylabel("Y")
    # представляем точки (х,у) кружочками диаметра 10
    plt.plot(x, y, 'r')

    # Сетка на фоне для улучшения восприятия
    plt.grid(True, linestyle='-', color='0.75')

    plt.show()


# получение ключа по value элемента в списке
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def calculate_height(heightsArray, struct):
    return list(map(lambda a, b: a + b, heightsArray, struct))


def chart_height_calculation(first_height, data):
    # результат высоты первой антенны
    result_first_height = 0
    # результат высоты второй антенны
    result_second_height = 0

    # координаты высот
    heightsArray = data['heightsArray']
    distanceArray = data['distanceArray']
    # координаты с учетом помех
    struct = data['struct']

    # считаем общие координаты
    height_result = calculate_height(heightsArray, struct)

    # график отображения координат для теста
    show_gr(distanceArray, height_result)

    # формируем dict с ключем id высоты в начальных данных
    height_dict = {}

    for enum, item in enumerate(height_result):
        height_dict[enum] = item

    # максимальная высота в списке координат
    height_max = max(height_result)
    result_first_height = height_max

    # ключ максимальной высоты в списке координат
    key_height = get_key(height_dict, height_max)

    if first_height == 0:
        result_second_height_right = get_right(height_result, key_height)
        result_second_height_left = get_left(height_result, key_height)

        if result_second_height_left > result_second_height_right:
            result_second_height = result_second_height_left
        else:
            result_second_height = result_second_height_right
    elif first_height > 0:
        result_first_height = first_height
        result_second_height_right = get_right(height_result, key_height)
        result_second_height_left = get_left(height_result, key_height)

        if result_second_height_left > result_second_height_right:
            result_second_height = result_second_height_left
        else:
            result_second_height = result_second_height_right
    else:
        print 'The height of the first antenna can not be negative.'

    print 'Height of the first antenna: %s' % result_first_height
    print'Height of the second antenna: %s' % result_second_height


if __name__ == '__main__':
    # данные для теста
    with open('data_test.json') as f:
        data = json.load(f)
    first_height = 0

    chart_height_calculation(0, data)
