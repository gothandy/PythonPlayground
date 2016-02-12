class TreeDict(object):

    def __init__(self, dict: dict):

        self.dict = dict

    def __getitem__(self, keys):

        return self._getdefault(keys)

    def getdefault(self, *keys, default=None):

        return self._getdefault(keys, default)

    def _getdefault(self, keys, default=None):

        d = self.dict

        for key in list(keys):

            if type(d) is not dict:
                break

            d = d.setdefault(key, default)

        return d




