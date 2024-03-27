# A Broker with a Stock Market Analysis Tool

This Python tool allows for the calculation of key stock market metrics, including the Dividend Yield, P/E Ratio, Volume Weighted Stock Price (VWSP), and the GBCE All Share Index for a predefined set of stocks.

## Features
- Calculate the Dividend Yield for a given stock.
- Compute the P/E Ratio for a given stock.
- Record trades for any stock, including timestamp, quantity, buy/sell indicator, and price.
- Calculate the Volume Weighted Stock Price for trades within the past 15 minutes.
- Calculate the GBCE All Share Index using the geometric mean of the volume weighted stock prices for all stocks.
## Getting Started

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system. You can download Python from python.org.

### Installation
Clone the repository to your local machine.

```bash
git clone https://github.com/ChuckTG/broker.git
cd broker
```
Usage
Calculating Stock Metrics
To use the tool for calculating stock metrics, import and create instances of the Stock class in broker.py. Here is a basic example:

```python
from broker import Stock

# Create a stock instance
stock = Stock('GIN', 'Preferred', 8, 0.02, 100)

# Record some trades
stock.record_trade(100, 'buy', 105)
stock.record_trade(200, 'sell', 110)

# Calculate Dividend Yield
print(f"Dividend Yield: {stock.dividend_yield(105)}")

# Calculate P/E Ratio
print(f"P/E Ratio: {stock.pe_ratio(105)}")

# Calculate Volume Weighted Stock Price
print(f"Volume Weighted Stock Price: {stock.volume_weighted_stock_price()}")
```
Calculating the GBCE All Share Index
To calculate the GBCE All Share Index for a list of stocks:

```python
from broker import Stock, calculate_gbce_all_share_index

# Assuming stocks is a list of Stock instances
print(f"GBCE All Share Index: {calculate_gbce_all_share_index(stocks)}")
```
## Running Tests


To run tests use the following command:

```bash
python -m unittest tests/test_broker.py
```
