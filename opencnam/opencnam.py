"""A simple python library for getting caller ID name information."""


__author__ = 'Randall Degges'
__copyright__ = 'Telephony Research Services, LLC'
__credits__ = ('Randall Degges', )

__license__ = 'UNLICENSE'
__version = '0.1'
__maintainer__ = 'Randall Degges'
__email__ = 'rdegges@gmail.com'
__status__ = 'Development'


class Phone(object):
    """An object that holds a single phone's information.

    :attr str number: The validated 10-digit US phone number.
    :attr str cnam: The caller ID name for this phone.
    """

    def __init__(self, number):
        self.cnam = ''
        self.number = self._parse_number(str(number))
