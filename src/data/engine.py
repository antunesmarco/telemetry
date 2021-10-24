from .fuel_pump import FuelPump
from .logger import logconf


logger = logconf('../../data/raw/rocket.log')


class Engine(object):

    def __init__(self):
        self._fuel_pump = FuelPump()
        logger.info(f'Engine created')

    def burn_fuel(self):
        pass

    def ignite(self):
        self._fuel_pump.get_fuel(1)

