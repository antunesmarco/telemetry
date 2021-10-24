import Fuel_tank


class FuelPump(object):

    def __init__(self, fuel_tank):
        self._fuelTank = fuel_tank

    def get_fuel(self, qty):
        return self._fuelTank.send_fuel(qty)
