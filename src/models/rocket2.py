import logging


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler(__name__ + '.log', mode='w')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)


class Rocket(object):

    def __init__(self, dry_mass=1, fuel=0):
        self._stage = 'standing'  # ["standing", "liftoff", "MECO", "apogee", "fairing", "parachute", "landing"]
        self._fuel_mass = fuel  # Kg
        self._dry_mass = dry_mass  # Kg
        self._wet_mass = self._dry_mass + self._fuel_mass
        self._burn_rate = 0.334  # Kg/s este motor queima 1Kg de combustível em 3 segundos
        self._thrust = 0  # N
        self._bar = 1  # Bar
        self._altitude = 0  # metros
        self._velocity = 0  # m/s
        self._lat = 0
        self._long = 0
        self._pitch = 0
        self._yaw = 0
        self._roll = 0
        self._radio_state = 'off'

    def __repr__(self):
        return "Rocket('" + self._stage + "', " + \
               str(self._velocity) + ", " + \
               str(self._fuel_mass) + ", " + \
               str(self._wet_mass) + ", " + \
               str(self._altitude) + ", " + \
               str(self._lat) + ", " + \
               str(self._long) + ", " + \
               str(self._pitch) + ", " + \
               str(self._yaw) + ", " + \
               str(self._roll) + ", " + \
               self._radio_state + ")"

    def ignite(self):
        if self._stage == 'standing':
            self._stage = 'liftoff'
            logger.info(f'Stage = {self._stage}')
            self.turn_on_engine()
        else:
            logger.info(f'Denied! Rocket is in stage: {self._stage}. Not Standing!')

    def turn_on_engine(self):
        logger.info(f'Fuel Level: {self._fuel_mass}')
        if self._fuel_mass > 0:
            logger.info('Engine ON!')
            self.burn_fuel()
        else:
            logger.warning('Out of gas!')

    def burn_fuel(self):
        if self._fuel_mass > 0:
            self._fuel_mass -= self._burn_rate if self._burn_rate <= self._fuel_mass else self._fuel_mass
            logger.info(f'Fuel burning! Fuel Level: {self._fuel_mass}')
            self._thrust = 25  # N

            if self._fuel_mass == 0:
                logger.info('Fuel burned!')
                self._stage = "MECO"
                logger.info(f'Stage: {self._stage}')

    def send_data(self):
        data = {
            "stage": self._stage,
            "velocity": self._velocity,
            "fuel": self._fuel_mass,
            "dry_mass": self._dry_mass,
            "wet_mass": self._wet_mass,
            "burn_rate": self._burn_rate,
            "thrust": self._thrust,
            "bar": self._bar,
            "altitude": self._altitude,
            "lat": self._lat,
            "long": self._long,
            "pitch": self._pitch,
            "yaw": self._yaw,
            "roll": self._roll,
            "radio_state": self._radio_state
        }
        return data
