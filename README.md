# python-opencnam

A simple python library for getting caller ID name information.

![OpenCNAM](https://www.opencnam.com/static/images/opencnam-logo-color-v2.png)

This library uses [OpenCNAM](https://www.opencnam.com "opencnam") as a backend.

[![Build Status](https://secure.travis-ci.org/telephonyresearch/python-opencnam.png?branch=master)](http://travis-ci.org/telephonyresearch/python-opencnam)


## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    $ pip install opencnam

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or you can [download the source code](https://github.com/telephonyresearch/python-opencnam/zipball/master "OpenCNAM
source code") for `OpenCNAM`, and then run:

    $ python setup.py install

You may need to run the above commands with `sudo`.


## Usage

Using `python-opencnam` is easy::

    from opencnam import Phone

    phone = Phone('+16284003994')
    print phone.number, phone.cnam


The main object, ``Phone``, defined in the ``opencnam`` module accepts a phone
number as input, and (behind the scenes) queries the
[opencnam](http://www.opencnam.com "opencnam") API to set the ``Phone.cnam``
attribute.

## API Authentication

To specify your API credentials, just pass them into the ``Phone`` constructor,
like so:

    from opencnam import Phone

    phone = Phone('+16284003994', account_sid='ACxxx', auth_token='AUxxx')

## Changelog

v06: 2018-11-30

    - Use OpenCNAM v3.
    - Support only `account_sid` and `auth_token` for authentication,
      removing the deprecated `api_user` and `api_key`.
    - Support Python 2.7 and Python 3.7

v0.5: 2012-11-08

    - Add support for OpenCNAM V2 API.
    - Deprecate the `api_user` and `api_key` authentication parameters,
      in favor of `account_sid` and `auth_token`.

v0.4: 2012-07-10

    - Add 3 second timeout to CNAM lookups, so we won't block for too long.

v0.3: 2012-07-09

    - Rewrite the backend to use ``requests`` instead of ``slumber``.
    - Clean up documentation.
    - Add public tests via Travis CI.

v0.2: 2012-03-19

    - Support API authentication.

v0.1: 2012-02-26

    - Initial release!
