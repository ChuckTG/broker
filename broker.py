from __future__ import annotations  # added for support of python versions < 3.10
import math
import datetime


class Broker:
    pass


class Trade:
    """
    Represents a trade of stock, including details such as quantity, price, and timestamp.

    Attributes:
        quantity (float): The quantity of stocks traded.
        indicator (str): An indicator specifying whether the trade was a buy or a sell.
        price (float): The price at which each stock was traded.
        timestamp (float | datetime.datetime): The datetime or timestamp when the trade occurred.
    """
    def __init__(self, quantity: float, indicator:str, price:float, timestamp: float | datetime.datetime | None = None):
        """
        Initializes a new instance of the Trade class.

        :param quantity: The quantity of the stock traded.
        :param indicator: The indicator of the trade, typically 'buy' or 'sell'.
        :param price: The trade price per stock unit.
        :param timestamp: The timestamp at which the trade took place. This can be a UNIX timestamp (as float),
                          a datetime object, or None. If None, the current time is used. If a float is provided,
                          it's converted to a datetime object.
        """
        self.quantity = quantity
        self.indicator = indicator
        self.price = price

        if isinstance(timestamp, float):
            self.timestamp = datetime.datetime.fromtimestamp(timestamp)
        else:
            self.timestamp = timestamp if timestamp else datetime.datetime.now()


class Stock:
    """
    The class to Represent a single Stock

     Attributes:
        symbol (str): The stock symbol.
        stock_type (str): The type of stock, either "Common" or "Preferred".
        last_dividend (float): The last dividend value.
        fixed_dividend (float): The fixed dividend value (for preferred stocks).
        par_value (float): The par value of the stock.
        trades (list[Trade]): A list of trades executed for this stock.
    """

    def __init__(self, symbol: str, stock_type: str, last_dividend: float, fixed_dividend: float,
                 par_value: float, ):
        """
          Initializes a new instance of the Stock class.

          :param symbol: The symbol representing the stock.
          :param stock_type: The type of the stock ("Common" or "Preferred").
          :param last_dividend: The last known dividend value of the stock.
          :param fixed_dividend: The fixed dividend percentage (for preferred stocks).
          :param par_value: The par value of the stock.
          """

        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades: [Trade] = []

    def dividend_yield(self, price: float) -> None | float:
        """
        Method that calculates the dividend yield of the Stock
        :param price (float): The price of the stock
        :return (float | None): returns the calculated dividend yield for the stock
        """
        if price <= 0:
            return None
        if self.stock_type == "Common":
            return self.last_dividend / price
        elif self.type == "Preffered":
            return (self.fixed_dividend * self.par_value) / price
        else:
            return None

    def pe_ratio(self, price: float) -> float | None:
        """
        Method that calculates the P/E ration of the stock

        :param price(float): The price of the stock
        :return: returns the calculated P/E Ratio of the stock
        """

        dividend = self.dividend_yield(price)

        if dividend == 0:
            return None
        else:
            return price / dividend

    def record_trade(self, quantity: float, indicator: int, price: float, timestamp=None):


        """
        Method that is used to record all trades of a given stock sequentially

        :param timestamp(float | datetime): The timestamp or datetime of the current trade
        :param quantity: the trade quantity of the stock
        :param indicator(str): A string that is either 'buy' or 'sell'
        :param price(float): The trade price for the stock

        """
        trade = Trade(quantity, indicator, price, timestamp)
        self.trades.append(trade)

    def volume_weighted_stock_price(self):
        """
        Method that calculates the Volume Weighted Stock Price

        :return(float |None ): Returns the calculated volume weighted stock price
        """
        relevant_trades = [trade for trade in self.trades if (datetime.datetime.now() - trade.timestamp).seconds <= 900]
        total_quantity = sum(trade.quantity for trade in relevant_trades)
        total_trade_price_quantity = sum(trade.price * trade.quantity for trade in relevant_trades)
        return None if total_quantity == 0 else total_trade_price_quantity / total_quantity


def calculate_gbce_all_share_index(stocks: [Stock]) -> float | None:
    """
    The main function of the broker module that calculates the GGCE all share index for all stocks

    :param stocks(Stock): a list of Stock instances
    :return(float | None): Returns the calculated GCCE ALL Share Index using the geometric mean of prices for all Stocks
    """
    prices = [stock.volume_weighted_stock_price() for stock in stocks if
              stock.volume_weighted_stock_price() is not None]
    if not prices:
        return None
    product = math.prod(prices)
    return product ** (1 / len(prices))
