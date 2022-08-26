import unittest

from battery import *
from utility import add_years_to_date

class TestSpinderBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today, -3)

        battery = SpinderBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today, -1)

        battery = SpinderBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today, -5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today, -3)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
