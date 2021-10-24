import datetime
from .logger import logconf


logger = logconf('../../data/raw/rocket.log')

class RocketLog(object):

    def __init__(self):
        self._buffer = []
        logger.info(f'RocketLog created')

    def write(self, source, event):
        msg = {'timestamp': datetime.datetime.now(), 'source': source, 'event': event}
        self._buffer.append(msg)
        logger.info(f'self._buffer: {self._buffer}')

    def read(self):
        logger.info(f'self._buffer: {self._buffer}')
        return self._buffer
