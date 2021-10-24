from .logger import logconf


logger = logconf('../../data/raw/rocket.log')


class RadioMedium(object):

    def __init__(self):
        self._buffer = []
        logger.info(f'RadioMedium created')

    def receive_radio(self, info):
        self._buffer = info
        logger.info(f'self._buffer: {self._buffer}')

    def get_radio(self):
        logger.info(f'self._buffer: {self._buffer}')
        return self._buffer
