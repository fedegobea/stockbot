# -*- coding: utf-8 -*-
import pandas_datareader.data as web

class StockPrice:
  ticker: str
  daily_close_prices: list[float]
  def __init__(self:StockPrice, ticker: str) -> None:
    self.ticker = ticker
    