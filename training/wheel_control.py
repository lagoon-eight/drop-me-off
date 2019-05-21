from picar import back_wheels, front_wheels
import picar
import threading

class TurnWheels():

    def __init__(self):
        self.fw = front_wheels.Front_Wheels(debug=True)
        self.max_right = 135
        self.max_left = 45
        self.straight = 90
        self.current_angle = 90
        self.direction = 1
        self.delta = 5 # number of degrees per turn
        picar.setup()

    def turn_wheels(self):
        if (self.current_angle >= self.max_right):
            self.current_angle = self.max_right
            self.direction = -1
        if (self.current_angle <= self.max_left):
            self.current_angle = self.max_left
            self.direction = 1

        self.current_angle = self.current_angle + (self.delta * self.direction)
        self.fw.wheel.write(self.current_angle)
        threading.Timer(1, self.turn_wheels).start()


tw = TurnWheels()
tw.turn_wheels()



