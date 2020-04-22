# coding=utf-8


class AlarmSensor(object):
    @staticmethod
    def run():
        print 'Alarm Ring...'


class WaterSprayer(object):
    @staticmethod
    def run():
        print 'Spray Water...'


class EmergencyDialer(object):
    @staticmethod
    def run():
        print 'Dial 119...'


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprayer = WaterSprayer()
        self.emergency_dialer = EmergencyDialer()

    def run(self):
        self.alarm_sensor.run()
        self.water_sprayer.run()
        self.emergency_dialer.run()


if __name__ == '__main__':
    emergency_facade = EmergencyFacade()
    emergency_facade.run()
