from unittest import TestCase
import unittest
from mock import patch, MagicMock
from test import T1
import test


class TestSimple(TestCase):
    @patch("test.T1.foo", MagicMock(return_value="abc"))
    def test_1(self):
        result = T1().get_foo()
        self.assertEqual(result, "abc")

    @patch('test.bar')
    def test_2(self, mock_obj):
        mock_obj.return_value = 'patched'
        value = test.bar()
        self.assertEqual('patched', value)

    # patch works from bottom to top
    @patch('test.T1.get_foo', MagicMock(return_value="abc"))
    @patch('test.T1.foo', MagicMock(return_value="abcde"))
    def test_3(self):
        value = T1().get_foo()
        self.assertEqual('abc', value)


unittest.main()
