"""OpenCNAM exceptions."""


class OpenCNAMError(Exception):
    """Generic OpenCNAM error."""
    pass


class InvalidPhoneNumberError(OpenCNAMError):
    """Phone number is invalid. Phone numbers must be at least 10-digits in
    length.
    """
    pass
