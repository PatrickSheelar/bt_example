import unittest
from bt_example import backtest

class TestBacktest(unittest.TestCase):

    def test_run_backtest(self):
        # Run the backtest and check for exceptions
        try:
            backtest.run_backtest()
        except Exception as e:
            self.fail(f"run_backtest() raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
