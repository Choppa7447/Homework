#!/usr/bin/env python
# -*- coding: utf-8 -*-
# есть список животных в зоопарке

zoo = ['lion','bear', 'kangaroo', 'elephant', 'monkey' ]
birds = ['rooster', 'ostrich', 'lark']

del zoo[3]
set = zoo + birds
print('Лев сидит в клетке № ',set.index('lion'), '\nЖаворонок сидит в клетке № ', set.index('lark'))

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код


