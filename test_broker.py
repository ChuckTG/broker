import unittest
from broker import Stock, calculate_gbce_all_share_index
from datetime import  datetime, timedelta

class TestStockMarket(unittest.TestCase):
    def setUp(self):
        # Setup stocks before each test method
        self.stocks = [
            Stock('TEA', 'Common', 0, None, 100),
            Stock('POP', 'Common', 8, None, 100),
            Stock('ALE', 'Common', 23, None, 60),
            Stock('GIN', 'Preferred', 8, 0.02, 100),
            Stock('JOE', 'Common', 13, None, 250)
        ]

    def test_record_trades(self):
        # Record some trades
        self.stocks[0].record_trade(100, 'buy', 105)
        self.stocks[1].record_trade(200, 'sell', 110)

        # Verify the trades were recorded correctly
        self.assertEqual(len(self.stocks[0].trades), 1)
        self.assertEqual(self.stocks[0].trades[0].quantity, 100)
        self.assertEqual(self.stocks[0].trades[0].indicator, 'buy')
        self.assertEqual(self.stocks[0].trades[0].price, 105)

        self.assertEqual(len(self.stocks[1].trades), 1)
        self.assertEqual(self.stocks[1].trades[0].quantity, 200)
        self.assertEqual(self.stocks[1].trades[0].indicator, 'sell')
        self.assertEqual(self.stocks[1].trades[0].price, 110)

    def test_gbce_all_share_index(self):
        # Assuming each stock has a recorded trade with its last price
        for stock in self.stocks:
            stock.record_trade(100, 'buy', 105)

        gbce_index = calculate_gbce_all_share_index(self.stocks)
        self.assertIsNotNone(gbce_index)
        self.assertTrue(gbce_index > 0)

class TestVolumeWeightedStockPrice(unittest.TestCase):
    def setUp(self):
        self.stock = Stock('TEST', 'Common', 0, None, 100)

    def test_vwsp_within_15_minutes(self):
        # Record trades within the last 15 minutes
        self.stock.record_trade(100, 'buy', 200, datetime.now() - timedelta(minutes=5))
        self.stock.record_trade(200, 'sell', 150, datetime.now() - timedelta(minutes=10))
        # Record a trade outside the 15-minute window
        self.stock.record_trade(50, 'buy', 100, datetime.now() - timedelta(minutes=20))
        expected_vwsp = ((100 * 200) + (200 * 150)) / (100 + 200)  # Calculate expected VWSP
        print(len(self.stock.trades))
        self.assertAlmostEqual(self.stock.volume_weighted_stock_price(), expected_vwsp, places=2, msg="VWSP calculation within 15 minutes is incorrect")


if __name__ == '__main__':
    unittest.main()
