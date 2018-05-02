# python-opencnam

A simple python library for getting caller ID name information.

![OpenCNAM](https://www.opencnam.com/static/images/opencnam-logo-color-v2.png)

This library uses [opencnam](https://www.opencnam.com "opencnam") as a backend.

[![Build Status](https://secure.travis-ci.org/telephonyresearch/python-opencnam.png?branch=master)](http://travis-ci.org/telephonyresearch/python-opencnam)


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


## API Authentication

If you've got an account on [opencnam](http://www.opencnam.com "opencnam"), you
can use your API credentials with python-opencnam. This will allow you to make
an unlimited amount of API queries (since paid users have no limits).

To specify your API credentials, just pass them into the ``Phone`` constructor,
like so:

    from opencnam import Phone

    phone = Phone('+18182179229', account_sid='ACxxx', auth_token='AUxxx')

Assuming you've specifid both the ``api_user`` and ``api_key`` params,
python-opencnam will use your credentials and you'll be running in no time!

**NOTE**: The ``api_user`` and ``api_key`` parameters are deprecated as of the
0.5 release. In the 0.6 release they will be removed.


## Limits

The [opencnam](http://www.opencnam.com "opencnam") API we use as a backend
limits you to no more than 60 requests per hour (using their free tier).


## Changelog

v0.5: 11-8-2012

    - Adding support for OpenCNAM V2 API.
    - Deprecating the ``api_user`` and ``api_key`` authentication parameters,
      these have been replaced by their new counterparts: ``account_sid`` and
      ``auth_token``.

v0.4: 7-10-2012

    - Adding 3 second timeout to CNAM lookups, this way we won't block for too
      long.

v0.3: 7-9-2012

    - Rewriting the backend to use ``requests`` instead of ``slumber``.
    - Cleaning up documentation.
    - Adding public tests via Travis CI.

v0.2: 3-19-2012

    - Adding support for API authentication.

v0.1: 2-26-2012

    - Initial release!
