# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Ограничение: Все задания надо выполнять используя только пройденные темы.
# """
# from sys import argv

# with open(argv[1], "r") as f:
#     for line in f:
#         if (( not line.strip().endswith('!') ) and ( not line.strip().startswith('!') ) ) :
#             print(line.rstrip())

from sys import argv


with open(argv[1], 'r') as f:
    for line in f:
        if line.find('!') == -1:
            print(line.strip('\n'))




