# -*- coding: utf-8 -*-
from ..price_retriever.stock_price import StockPrice

def get_stock_price(ticker=False):
  if not ticker:
    print('No se envio un ticker')
  stock_price = StockPrice(ticker)
  return stock_price
