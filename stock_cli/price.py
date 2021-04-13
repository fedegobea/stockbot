# -*- coding: utf-8 -*-
from ..price_retriever.stock_price import StockPrice

def get_stock_price(ticker=False, periods=20):
  if not ticker:
    print('No se envio un ticker')
  stock_price = StockPrice(ticker, periods)
  return stock_price
