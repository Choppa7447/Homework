#!/usr/bin/env python3
# -*- coding: utf-8 -*-
my_favorite_movies = ['Терминатор', 'Пятый элемент', 'Аватар', 'Чужие', 'Назад в будущее']

# Есть строка с перечислением фильмов
# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с концa

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
set = my_favorite_movies
print(set[0], set[4], set[1], set[-2])