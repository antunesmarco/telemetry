def get_bar():
    reading =
    return reading


class Sensor(object):

    def __init__(self, type, Log):
        self._type = type  # ["barometer", "gps", "accelerometer"]
        self._log = Log

    def get_sensor_value(self):
        readings = {"barometer": get_bar(), "gps": get_gps(), "accelerometer": get_accel()}
        value = readings[self._type]
        return value

    def read_sensor(self):
        reading = self.get_sensor_value()
        return reading
