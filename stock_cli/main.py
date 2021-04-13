# -*- coding: utf-8 -*-
from .price import get_stock_price


print('Hola')
ticker = input('El precio de que accion queres obtener?')
print(get_stock_price(ticker))


