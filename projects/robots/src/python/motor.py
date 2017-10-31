m = ev3.LargeMotor('outA')
m.connected
m.run_timed(time_sp=3000, speed_sp=720)
while True:
    print(m.position)
