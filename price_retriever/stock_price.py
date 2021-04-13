# -*- coding: utf-8 -*-
import pandas_datareader.data as web

class StockPrice:

  ticker: str
  daily_close_prices: list[float]

  def _stock_closes(self: StockPrice, periods:int) -> list[float]:
    stock_info = web.DataReader(self.ticker,'stooq')
    return stock_info['Close'].to_list()[-periods:]

  def __init__(self: StockPrice, ticker: str, periods:int=20) -> None:
    self.ticker = ticker
    self.daily_close_prices = self._stock_closes(periods)

  def __repr__(self: StockPrice) -> str:
    prices = self.daily_close_prices
    return 'StockPrice({ticker} | {periods} Periodos | Precios: {prices})'.format(ticker=self.ticker, periods=len(prices), prices=','.join(prices))

