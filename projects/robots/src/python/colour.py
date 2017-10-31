cs = ev3.ColorSensor(ev3.INPUT_4)
cs.connected
cs.mode = 'COL-COLOR'
while True:
    print(cs.value())
