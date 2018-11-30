from unittest import TestCase

from opencnam import InvalidPhoneNumberError, Phone


class PhoneTest(TestCase):

    def test_init_requires_number(self):
        self.assertRaises(TypeError, Phone)

#    def test_init_attempts_to_lookup_cnam(self):
#       TODO: Mock and make sure that Phone.get_cnam() was called one time.

    def test_init_sets_number_after_validation(self):
        phone = Phone('8182179229', account_sid='ACxxxx', auth_token='AUxxxx')
        self.assertEqual(phone.number, '8182179229')

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
