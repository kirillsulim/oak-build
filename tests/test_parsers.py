from enum import Enum, auto
from unittest import TestCase

from oak_build.parsers import parse_enum, parse_int, parse_bool


class TestEnum(Enum):
    VALUE_A = auto()
    VALUE_B = auto()


class TestEnumParser(TestCase):
    def test_parse_simple_enum_value(self):
        ok_result = parse_enum("VALUE_A", TestEnum)

        self.assertTrue(ok_result.is_ok)
        self.assertEqual(TestEnum.VALUE_A, ok_result.unwrap())

    def test_return_error_when_no_such_value(self):
        err_result = parse_enum("MISSING_VALUE", TestEnum)

        self.assertTrue(err_result.is_err)
        self.assertListEqual(
            ["Unknown value MISSING_VALUE, allowed values are VALUE_A, VALUE_B"],
            err_result.unwrap_err()
        )


class TestIntParser(TestCase):
    def test_parse_int_value(self):
        ok_result = parse_int("123")

        self.assertTrue(ok_result.is_ok)
        self.assertEqual(123, ok_result.unwrap())

    def test_return_error_when_incorrect_int(self):
        err_result = parse_int("abc")

        self.assertTrue(err_result.is_err)
        self.assertListEqual(
            ["Cannot parse \"abc\" as int"],
            err_result.unwrap_err()
        )


class TestBoolParser(TestCase):
    def test_parse_int_value(self):
        ok_result = parse_bool("True")

        self.assertTrue(ok_result.is_ok)
        self.assertEqual(True, ok_result.unwrap())

    def test_return_error_when_incorrect_boolean(self):
        err_result = parse_bool("abc")

        self.assertTrue(err_result.is_err)
        self.assertListEqual(
            ["Unknown value abc, allowed values are true, t, yes, y, false, f, no, n"],
            err_result.unwrap_err()
        )

