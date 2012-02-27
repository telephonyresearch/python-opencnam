"""Some hack-ish helpers."""


from requests import session
from slumber import API as SlumberAPI


class API(SlumberAPI):
    """A temporary wrapper around Slumber's API class. This is due to
    https://github.com/dstufft/slumber/pull/12.

    Once this pull request is merged (and the bug fixed), I'll revert to using
    Slumber's native API class.
    """
    def __init__(self, base_url=None, auth=None, format=None,
            append_slash=True):
        super(API, self).__init__(base_url, auth, format, append_slash)
        self._store['session'] = session(auth=auth, headers={'Accept':
            'application/json'})
