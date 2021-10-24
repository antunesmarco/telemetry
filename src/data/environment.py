from .radio_medium import RadioMedium
from .logger import logconf


logger = logconf('../../data/raw/rocket.log')


class Environment(object):

    def __init__(self, g=9.8):
        self._g = g  # m/s**2
        self._radio_medium = RadioMedium()
        logger.info(f'Environment created')

    def react(self, net_force, altitude):
        pass
        return

    def calc_force(self, m1, m0, v1, v0, t1, t0):
        return (m1 * v1 - m0 * v0) / (t1 - t0)

    def calc_alt(self):
        m * (dv/dt) = rve - mg

        return