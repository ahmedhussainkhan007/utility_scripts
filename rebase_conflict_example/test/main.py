import unittest

from your_program import simple_interest  # Assuming your program is in a separate file

class TestSimpleInterest(unittest.TestCase):

  def test_positive_values(self):
    """Tests simple_interest with positive values."""
    principal = 10000
    rate = 0.05
    time = 2
    expected_interest = 1000

    actual_interest = simple_interest(principal, rate, time)
    self.assertEqual(expected_interest, actual_interest)

  def test_zero_rate(self):
    """Tests simple_interest with zero interest rate."""
    principal = 10000
    rate = 0.0
    time = 2
    expected_interest = 0

    actual_interest = simple_interest(principal, rate, time)
    self.assertEqual(expected_interest, actual_interest)

  def test_zero_time(self):
    """Tests simple_interest with zero time period."""
    principal = 10000
    rate = 0.05
    time = 0
    expected_interest = 0

    actual_interest = simple_interest(principal, rate, time)
    self.assertEqual(expected_interest, actual_interest)

if __name__ == '__main__':
  unittest.main()
impot unittest
def test_function ():
    pass
