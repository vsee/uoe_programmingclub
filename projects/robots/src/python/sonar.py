us = ev3.UltrasonicSensor(ev3.INPUT_4)
us.connected
us.mode = 'US-DIST-CM'
while True:
    print(us.value())
