from .radio_medium import RadioMedium
from .logger import logconf


logger = logconf('../../data/raw/rocket.log')
bslogger = logconf('../../data/raw/base_station.log')


class BaseStation(object):

    def __init__(self):
        self._buffer = []
        self._radio_medium = RadioMedium()
        logger.info(f'BaseStation created')

    def save_info(self):
        bslogger.info(f'info: {self._buffer}')
        logger.info(f'self._buffer: {self._buffer}')

    def turn_on_radio(self):
        self._buffer = self._radio_medium.get_radio()
        self.save_info()
        logger.info(f'turn_on_radio')

