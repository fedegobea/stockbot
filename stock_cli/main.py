# -*- coding: utf-8 -*-
from .price import get_stock_price


print('Hola')
ticker = input('¿El precio de que accion queres obtener?')
periods = input('¿Que periodos quisera ver?')
print(get_stock_price(ticker))




