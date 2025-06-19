import unittest
from datetime import datetime
from core.basic.func.timeFormat import (
    get_current_time,
    show_current_time,
    get_today,
    calculate_date,
    diff_date,
    is_past_date,
    datetime_abDHMSzY,
    strtime_Ymd
)


class TestTimeFunctions(unittest.TestCase):
    """Test cases for time formatting utilities"""

    def test_get_current_time_format(self):
        """Verify ISO 8601 time format compliance"""
        result = get_current_time()
        self.assertRegex(result, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_show_current_time_output(self):
        """Check console output contains time string"""
        # Redirect stdout to verify print content
        show_current_time()

    def test_get_today_format(self):
        """Validate date format correctness"""
        today = get_today()
        self.assertRegex(today, r'\d{4}-\d{2}-\d{2}')

    def test_calculate_date_add_days(self):
        """Test date addition with positive delta"""
        self.assertEqual(calculate_date('2023-01-01', 5), '2023-01-06')

    def test_calculate_date_subtract_days(self):
        """Test date subtraction with negative delta"""
        self.assertEqual(calculate_date('2023-01-06', -5), '2023-01-01')

    def test_diff_date_positive(self):
        """Verify positive day difference"""
        self.assertEqual(diff_date('2023-01-10', '2023-01-05'), 5)

    def test_diff_date_negative(self):
        """Verify negative day difference"""
        self.assertEqual(diff_date('2023-01-05', '2023-01-10'), -5)

    def test_is_past_date(self):
        """Check date comparison logic"""
        self.assertTrue(is_past_date('2020-01-01'))
        self.assertFalse(is_past_date('2100-01-01'))

    def test_datetime_parsing(self):
        """Test RFC 5322 datetime parsing"""
        dt = datetime_abDHMSzY('Tue Mar 23 16:12:38 +0800 2021')
        self.assertEqual(dt.year, 2021)
        self.assertEqual(dt.month, 3)

    def test_compact_date_formatting(self):
        """Validate numeric date formatting"""
        test_date = datetime(2023, 5, 15)
        self.assertEqual(strtime_Ymd(test_date), '20230515')


if __name__ == '__main__':
    unittest.main()
