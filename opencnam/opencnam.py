"""A simple python library for getting caller ID name information."""


from re import sub

from requests import get
from requests.exceptions import ConnectionError, Timeout

from .errors import InvalidPhoneNumberError


class Phone(object):
    """An object that holds a single phone's information.

    :attr str OPENCNAM_API_URL: Current OpenCNAM API endpoint.
    :attr str number: The validated 10-digit US phone number.
    :attr str cnam: The caller ID name for this phone.
    :attr str api_user: Your API username.
    :attr str api_key: Your API key.
    """
    OPENCNAM_API_URL = 'https://api.opencnam.com/v2/phone/%s'

    def __init__(self, number, cnam='', api_user=None, api_key=None,
            account_sid=None, auth_token=None):
        """Create a new Phone object, and attempt to lookup the caller ID name
        information using opencnam's public API.

        :param unicode number: The phone number to query in any format.
        :param unicode cnam: If you'd like to manually set the caller ID name
            for this phone number, you can do so here.
        :param str api_user: DEPRECATED. Your API username.
        :param str api_key: DEPRECATED. Your API key.
        :param str account_sid: Your Account SID (found in the OpenCNAM dashboard).
        :param str auth_token: Your Auth Token (found in the OpenCNAM dashboard).

        Usage::

            from opencnam import Phone

            phone = Phone('+18182179229')
            ...

        ..note::
            When a new Phone object is created, we'll attempt to clean up the
            phone number input to convert it into a usable format for use with
            opencnam's API.
        """
        self.cnam = unicode(cnam)
        self.number = unicode(number)
        self.api_user = api_user
        self.api_key = api_key
        self.account_sid = account_sid or self.api_user
        self.auth_token = auth_token or self.api_key

        # Clean up ``number``, and try to build a valid phone number that
        # opencnam can use.
        self.clean()

        # Attempt to grab the caller ID name information from opencnam. If we
        # can't get a caller ID response back, we won't retry (developers can
        # manually retry to grab the caller ID at any time using ``get_cnam``).
        self.get_cnam()

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
            params = {'format': 'pbx'}

            # If the user supplied API creds, use them.
            if self.account_sid and self.auth_token:
                params['account_sid'] = self.account_sid
                params['auth_token'] = self.auth_token

            try:
                response = get(self.OPENCNAM_API_URL % self.number, params=params, timeout=3)
                if response.status_code == 200:
                    self.cnam = response.text
            except (ConnectionError, Timeout):
                pass
