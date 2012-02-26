"""A simple python library for getting caller ID name information."""


__author__ = 'Randall Degges'
__copyright__ = 'Telephony Research Services, LLC'
__credits__ = ('Randall Degges', )

__license__ = 'UNLICENSE'
__version = '0.1'
__maintainer__ = 'Randall Degges'
__email__ = 'rdegges@gmail.com'
__status__ = 'Development'


from re import sub

from .errors import InvalidPhoneNumberError


class Phone(object):
    """An object that holds a single phone's information.

    :attr str number: The validated 10-digit US phone number.
    :attr str cnam: The caller ID name for this phone.
    """

    def __init__(self, number):
        self.cnam = ''
        self.number = self._parse_number(str(number))

    def _parse_number(self, number):
        """Make ``number`` a valid phone number and return it.

        :param str number: Phone number in any format.
        :rtype: string
        :returns: A valid 10-digit US phone number as a string.
        :raises: InvalidPhoneNumberError if ``number`` cannot be made into a
            valid US phone number.

        Usage::

            from opencnam import Phone

            phone = Phone('+1-818-217-9229')
            assert phone.number == '8182179229'
        """
        number = sub(r'\D', '', number)
        number = number[-10:]

        if len(number) < 10 or not (2002000000 <= long(number) <= 9999999999):
            raise InvalidPhoneNumberError

        return number

    def _get_cnam(self):
        """Query the OpenCNAM API and retreive the caller ID name string
        associated with this phone.
        """
        pass
