g = ev3.GyroSensor(ev3.INPUT_4)
g.connected
g.mode = 'GYRO-ANG'
while True:
    print(g.value())
