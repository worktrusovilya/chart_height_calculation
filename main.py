# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt


# получения максимума слева или справа
def get_max_section(section, xy, id_height_max):
    max = {}
    height_max_section = 0.0

    # срез от максимальной высоты
    if section == 'right':
        xy_section = xy[id_height_max + 1:]
    elif section == 'left':
        xy_section = xy[:id_height_max - 1]
    else:
        xy_section = xy

    # максимальная высота в списке координат
    for item in xy_section:
        if height_max_section < item['y']:
            height_max_section = item['y']
            max = item

    return max


# отображение графика координат для теста
def show_gr(x, y):
    plt.xlabel("X")
    plt.ylabel("Y")

    # представляем точки (х,у) кружочками диаметра 10
    plt.plot(x, y, 'r')

    # Сетка на фоне для улучшения восприятия
    plt.grid(True, linestyle='-', color='0.75')
    plt.show()


def calculate_height(heightsArray, struct):
    return list(map(lambda a, b: a + b, heightsArray, struct))


def chart_height_calculation(first_height, data):
    # результат высоты первой антенны
    result_first_height = 0
    # результат высоты второй антенны
    result_second_height = 0

    # координаты высот
    heightsArray = data['heightsArray']
    x = data['distanceArray']
    # координаты с учетом помех
    struct = data['struct']

    # считаем общие координаты
    y = calculate_height(heightsArray, struct)

    show_gr(x, y)

    # список dict координат
    xy = []
    for enum, x_item in enumerate(y):
        xy.append({'id': enum, 'y': x_item})

    for enum, item in enumerate(xy):
        xy[enum].update({'x': y[enum]})

    # максимальная высота
    height_max = 0.0
    max_center = {}

    # находим максимальную высоту
    for item in xy:
        if height_max < item['y']:
            height_max = item['y']
            max_center = item

    if first_height == 0:
        # максимальная высота справа от максимума
        max_right = get_max_section('right', xy, max_center['id'])
        # максимальная высота слева от максимума
        max_left = get_max_section('left', xy, max_center['id'])

        print(max_center)
        print(max_left)
        print(max_right)
    elif first_height > 0:
        pass
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
