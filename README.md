A simple python library for getting caller ID name information.

This library uses [opencnam](http://www.opencnam.com "opencnam") as a backend.


## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    $ pip install opencnam

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/telephonyresearch/python-opencnam/zipball/master "opencnam
source code") for `opencnam`, and then run:

    $ python setup.py install

You may need to run the above commands with `sudo`.


## Usage

Using `python-opencnam` is easy::

    from opencnam import Phone

    phone = Phone('2024561111')
    print phone.number, phone.cnam 


The main object, ``Phone``, defined in the ``opencnam`` module accepts a phone
number as input, and (behind the scenes) queries the
[opencnam](http://www.opencnam.com "opencnam") API to set the ``Phone.cnam``
attribute.

To make things insanely easy, ``python-opencnam`` transparently handles phone
number validation--so you can create a ``Phone`` object using any phone number
you can possibly imagine, as long as it can be cleaned up into a valid,
10-digit, US phone number.

For example::

    from opencnam import Phone

    phone = Phone('+1 (818)-217 \\\\9229')
    assert phone.number == '8182179229'

The way the number cleaning algorithm works is:

* Remove all non-integer characters.
* Grab the last 10 digts of the string.
* Make sure those 10 digits are a valid US phone number.

So you can go crazy with input, and not worry about getting an
``opencnam.InvalidPhoneNumberError`` exception unless the phone number cannot
be made valid.


## Limits

The [opencnam](http://www.opencnam.com "opencnam") API we use as a backend
limits you to no more than 60 requests per minute (using their free tier). When
they release a paid API, you'll have the option of specifying API creds to make
unlimited requests.


## Changelog

v0.1: 2-26-2012

- Initial release!
