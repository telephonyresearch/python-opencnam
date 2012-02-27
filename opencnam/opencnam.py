"""A simple python library for getting caller ID name information."""


from re import sub

from slumber.exceptions import HttpClientError, HttpServerError

from .errors import InvalidPhoneNumberError
from .helpers import API


class Phone(object):
    """An object that holds a single phone's information.

    :attr str OPENCNAM_API_URL: Current OpenCNAM API endpoint.
    :attr str number: The validated 10-digit US phone number.
    :attr str cnam: The caller ID name for this phone.
    """
    OPENCNAM_API_URL = 'https://api.opencnam.com/v1'

    def __init__(self, number):
        self.api = API(self.OPENCNAM_API_URL, append_slash=False)
        self.cnam = ''
        self.number = str(number)

        # Clean up ``number``, and try to build a valid phone number that
        # opencnam can use.
        self.clean()

    def clean(self):
        """Clean up ``number``, trying to make it a valid phone number that
        opencnam can use. opencnam only supports 10-digit US phone numbers with
        no symbols.

        :raises: InvalidPhoneNumberError if ``number`` cannot be made into a
            valid US phone number.

        Usage::

            from opencnam import Phone

            phone = Phone('+1-818-217-9229')
            assert phone.number == '8182179229'
        """
        self.number = sub(r'\D', '', self.number)
        self.number = self.number[-10:]

        if len(self.number) < 10 or not (2002000000 <= long(self.number) <= 9999999999):
            raise InvalidPhoneNumberError

    def get_cnam(self):
        """Query the OpenCNAM API and retreive the caller ID name string
        associated with this phone.

        Once we've got a valid caller ID name for this phone number, we'll
        cache that name for future reference.
        """
        if not self.cnam:
            try:
                self.number = self.api.phone(self.number).get()['cnam']
            except (HttpClientError, HttpServerError, KeyError):
                pass
        else:
            return self.cnam
