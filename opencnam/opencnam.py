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
    :attr str account_sid: Your Account SID.
    :attr str auth_token: Your Auth Token.
    """
    OPENCNAM_API_URL = 'https://api.opencnam.com/v3/phone/%s'

    def __init__(self, number, account_sid, auth_token, cnam=''):
        """Create a new Phone object, and attempt to lookup the caller ID name
        information using opencnam's public API.

        :param str number: The phone number to query in any format.
        :param str cnam: If you'd like to manually set the caller ID name
            for this phone number, you can do so here.
        :param str account_sid: Your Account SID (found in the OpenCNAM dashboard).
        :param str auth_token: Your Auth Token (found in the OpenCNAM dashboard).

        Usage::

            from opencnam import Phone

            phone = Phone('+18182179229')
            ...
        """
        self.cnam = cnam
        self.number = number
        self.account_sid = account_sid
        self.auth_token = auth_token

        # Attempt to grab the caller ID name information from opencnam. If we
        # can't get a caller ID response back, we won't retry (developers can
        # manually retry to grab the caller ID at any time using ``get_cnam``).
        self.get_cnam()

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
                    self.cnam = str(response.text)
            except (ConnectionError, Timeout):
                pass
