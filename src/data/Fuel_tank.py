class FuelTank(object):

    def __init__(self, vol=0):
        self._vol = vol

    def get_vol(self):
        return self._vol

    def send_fuel(self, qty_req):
        if self._vol >= qty_req:
            self._vol -= qty_req
            qty_sent = qty_req
        else:
            qty_sent = self._vol
            self._vol = 0

        return qty_sent
