''' Домашнее задание:
    1. Написать программу для работы пользователя со списком.

    Пользовательский интерфейс должен представлять из себя консольное меню из четырех пунктов:
        1 - Демонстрация списка
        2 - Добавление элемента в конец списка
        3 - Удаление последнего элемента из списка
        4 - Выход

    Программа ожидает ввод от пользователя числа от 1 до 4 для перехода к соответствующему действию.
    Реагировать на ввод любых других чисел программа не должна. При переходе к каждому из действий
    пункты меню стираются. Изначально список пуст.

    Дополнительные материалы:
    1. ДЗ+
        К вышеописанному ТЗ добавить пункт меню, осуществляющий сортировку массива, а также добавить
        ко 2 и 3 пунктам возможность добавлять(удалять) элемент по индексу, отдельно запрашиваемому у
        пользователя в соотв. подменю.
'''
import os
from termcolor import cprint

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def help():
    cls() # Очищаем консоль
    print('1 - Демонстрация списка',
          '2 - Добавление элемента в конец списка',
          '3 - Удаление последнего элемента из списка',
          '4 - Сортировка списка',
          '5 - Выход', sep='\n')

work_list = []  # Список
help()

while True:
    try:
        num = int(input("\nВведите число (1...5): "))
    except ValueError:
        cprint('Нужно было ввести число!', 'black', 'on_red')
        continue

    if num == 1:
        cls()
        cprint('1 - Демонстрация списка', 'red', 'on_blue')
        print('2 - Добавление элемента в конец списка',
              '3 - Удаление последнего элемента из списка',
              '4 - Сортировка списка',
              '5 - Выход', sep='\n')

        cprint('Наш список: ', 'black', 'on_light_yellow', end='')
        cprint(work_list, 'black', 'on_light_yellow', end=', ')
    elif num == 2:
        cls()
        print('1 - Демонстрация списка')
        cprint('2 - Добавление элемента в конец списка', 'red', 'on_blue')
        print('3 - Удаление последнего элемента из списка')
        print('4 - Сортировка списка')
        print('5 - Выход')

#        cprint('\nВведите новый элемент списка: ', 'yellow', end=' ')
#        work_list.append(input())
        cprint('\nВведите индекс нового элемента списка: ', 'yellow', end=' ')
        try:
            idx = int(input())
        except ValueError:
            cprint('Нужно было ввести число!', 'black',  'on_red')
        else:
            cprint('Введите новый элемент списка: ', 'green', end=' ')
            item = input()
            work_list.insert(idx, item)
            help()


    elif num == 3:
        cls()
        print('1 - Демонстрация списка')
        print('2 - Добавление элемента в конец списка')
        cprint('3 - Удаление последнего элемента из списка', 'red', 'on_blue')
        print('4 - Сортировка списка')
        print('5 - Выход')

#        work_list.pop()
        cprint('\nВведите индекс удаляемого элемента: ', 'yellow', end=' ')
        try:
            idx = int(input())
        except ValueError:
            cprint('Нужно было ввести число!', 'black', 'on_red')
        else:
            if idx < len(work_list):
                work_list.pop(idx)
            else:
                work_list.pop(len(work_list)-1)
            help()
    elif num == 4:
        work_list.sort()
        cprint('Список после сортировки: ', 'black', 'on_light_yellow', end='')
        cprint(work_list, 'black', 'on_light_yellow', end=', ')
    elif num == 5:
        break
    else:
        help()


#
# a = int(input("Input a number: "))
# print("My number is", a)

# if a > 0 and a % 2 == 0:
#     print('first version')
# elif a < 0:
#     print('second version')
# else:
#     print('third version')
#
# counter = 0
# while a > 0:
#     a = a - 5
#     counter += 1
#
# print(counter)

#
# for item in range(5, 10, 2):
#     print(item)

#
# def printColumn(array):
#     for item in array:
#         print(item)
#
#
#
# numbers = [3.12, 6.54, 7.65]
# printColumn(numbers)

'''
from random import *

a = randint(1, 10)
b = round(random(), 5)


print(a,b, choice(['Yes','No']))
'''