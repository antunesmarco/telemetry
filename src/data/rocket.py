import logging


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('rocket.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


class Rocket(object):

    def __init__(self, fuel=0):
        # "standing": True, "liftoff": False, "MECO": False, "apogee": False, "fairing": False, "parachute": False,
        # "landing": False
        self._stage = 'standing'
        self._speed = 0
        self._fuel = fuel
        self._weight = fuel
        self._altitude = 0
        self._lat = 0
        self._long = 0
        self._pitch = 0
        self._yaw = 0
        self._roll = 0
        self._radio_state = 'off'


    def __repr__(self):
        return "Rocket('" + self._stage + "', " + \
               str(self._speed) + ", " + \
               str(self._fuel) + ", " + \
               str(self._weight) + ", " + \
               str(self._altitude) + ", " + \
               str(self._lat) + ", " + \
               str(self._long) + ", " + \
               str(self._pitch) + ", " + \
               str(self._yaw) + ", " + \
               str(self._roll) + ", " + \
               self._radio_state + ")"

    def __str__(self):
        return "Stage: " + self._stage + \
               ", Speed: " + str(self._speed) + \
               ", Fuel: " + str(self._fuel) + \
               ", Weight: " + str(self._weight) + \
               ", Altitude: " + str(self._altitude) + \
               ", Lat: " + str(self._lat) + \
               ", Long: " + str(self._long) + \
               ", Pitch: " + str(self._pitch) + \
               ", Yaw: " + str(self._yaw) + \
               ", Roll: " + str(self._roll) + \
               ", Radio State: " + self._radio_state

    def ignite(self):
        if self._stage == 'Standing':
            self._stage = 'liftoff'
            logger.info(f'Stage = {self._stage}')
            self.turn_on_engine()
        else:
            logger.info(f'Denied! Rocket is in stage: {self._stage}. Not Standing!')

    def fuel_rocket(self, perc):
        if self._stage == 'Standing':
            self._fuel = perc
            self._weight += perc
            logger.info(f'Fuel loaded! Fuel level: {self._fuel} %. Weight: {self._weight}')
        else:
            logger.info(f'Denied! Rocket is in stage: {self._stage}. Not Standing')

    def burn_fuel(self):
        if self._fuel > 0:
            self._fuel -= 10
            logger.warning(f'Fuel burning! Fuel Level: {self._fuel}')

            self._weight -= 10
            logger.warning(f'Weight: {self._weight}')

            self._altitude += 120 - self._weight
            logger.warning(f'Altitude: {self._altitude}')

            self._speed += 120 - self._weight
            logger.warning(f'Speed: {self._speed}')
        else:
            logger.warning('Fuel burned!')
            self._stage = "MECO"
            logger.warning(f'Stage: {self._stage}')

            if self._speed > 0:
                self._speed -= 10
                logger.warning(f'Speed: {self._speed}')

                momentum = self._speed * 0.1
                self._altitude += momentum
                logger.warning(f'Altitude: {self._altitude}')

                self._speed += momentum
                logger.warning(f'Speed: {self._speed}')

            if self._altitude > 0:
                self._altitude -= self._speed if self._speed < self._altitude else self._altitude
                logger.warning(f'Altitude: {self._altitude}')
            else:
                self._speed = 0
                self._stage = "landing"
                logger.warning(f'Stage: {self._stage}. Altitude: {self._altitude}!')

    def turn_on_engine(self):
        if self._fuel > 0:
            logger.warning('Engine ON!')
        else:
            logger.warning('Out of gas!')

    def transmit_data(self):
        self.radio_state = 'on'
        # self.read_sensors()
        # self.send_data()

    def send_data(self):
        data = {
            "stage": [self._stage],
            "speed": self._speed,
            "fuel": self._fuel,
            "weight": self._weight,
            "altitude": self._altitude,
            "lat": self._lat,
            "long": self._long,
            "pitch": self._pitch,
            "yaw": self._yaw,
            "roll": self._roll,
            "radio_state": self._radio_state
        }
        return data

