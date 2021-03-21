from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires):
        self.name = name
        if NOW > expires:
            self._expired = True
        else:
            self._expired = False


    @property
    def expired(self):
        return self._expired
