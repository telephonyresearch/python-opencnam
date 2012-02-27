from unittest import TestCase

from opencnam import InvalidPhoneNumberError, Phone


class PhoneTest(TestCase):

    def test_init_requires_number(self):
        self.assertRaises(TypeError, Phone)

    def test_init_sets_empty_cnam(self):
        phone = Phone('8182179229')
        self.assertEqual(phone.cnam, '')

    def test_init_sets_number_after_validation(self):
        phone = Phone('8182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_parse_number_removes_non_ints(self):
        phone = Phone('8182179229a')
        self.assertEqual(phone.number, '8182179229')

        phone = Phone('a8182179229')
        self.assertEqual(phone.number, '8182179229')

        phone = Phone('   818   217   -9229')
        self.assertEqual(phone.number, '8182179229')

    def test_parse_number_raises_error_on_short_number(self):
        self.assertRaises(InvalidPhoneNumberError, Phone, '818217922')

    def test_parse_returns_only_last_10_digits_of_number(self):
        phone = Phone('11111111111111118182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_parse_number_returns_valid_number_untouched(self):
        phone = Phone('8182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_parse_number_catches_invalid_numbers(self):
        self.assertRaises(InvalidPhoneNumberError, Phone, '1001000000')
        self.assertRaises(InvalidPhoneNumberError, Phone, '2001999999')
