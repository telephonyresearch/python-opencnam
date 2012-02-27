from unittest import TestCase

from opencnam import InvalidPhoneNumberError, Phone


class PhoneTest(TestCase):

    def test_init_requires_number(self):
        self.assertRaises(TypeError, Phone)

#    def test_init_attempts_to_lookup_cnam(self):
#       TODO: Mock and make sure that Phone.get_cnam() was called one time.

    def test_init_sets_number_after_validation(self):
        phone = Phone('8182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_clean_removes_non_ints(self):
        phone = Phone('8182179229a')
        self.assertEqual(phone.number, '8182179229')

        phone = Phone('a8182179229')
        self.assertEqual(phone.number, '8182179229')

        phone = Phone('   818   217   -9229')
        self.assertEqual(phone.number, '8182179229')

    def test_clean_raises_error_on_short_number(self):
        self.assertRaises(InvalidPhoneNumberError, Phone, '818217922')

    def test_clean_only_last_10_digits_of_number(self):
        phone = Phone('11111111111111118182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_clean_returns_valid_number_untouched(self):
        phone = Phone('8182179229')
        self.assertEqual(phone.number, '8182179229')

    def test_clean_catches_invalid_numbers(self):
        self.assertRaises(InvalidPhoneNumberError, Phone, '1001000000')
        self.assertRaises(InvalidPhoneNumberError, Phone, '2001999999')

#    def test_get_cnam_doesnt_lookup_cnam_if_cnam_is_already_set(self):
#       TODO: Mock and make sure that once Phone.cnam is set, calls to
#       Phone.get_cnam() don't make any API calls and use the cached cnam
#       instead.

#   def test_get_cnam_sets_cnam(self):
#       TODO: Mock and make sure that once Phone.get_cnam() is called, it
#       actually updates Phone.cnam with the value.

#   def test_get_cnam_doesnt_do_anything_on_error(self):
#       TODO: Mock and make sure that if the API call fails to opencnam, that
#       Phone.get_cnam() doesn't do anything and leaves Phone.cnam alone.
