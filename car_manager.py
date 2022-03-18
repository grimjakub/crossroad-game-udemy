from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_X = 300
MAX_Y = 200
STEPS_X=list(range(-MAX_X,MAX_X+40,40))
STEPS_Y=list(range(-MAX_Y,MAX_Y+20,20))


class CarManager():
    def __init__(self):
        # super().__init__()
        self.cars = []
        self.generate_cars_start(15)
        self.count = 0
        self.move_speed=STARTING_MOVE_DISTANCE

    def make_car(self, start_x):
        new_car = Turtle("square")
        new_car.penup()
        start_y = random.choice(STEPS_Y)
        new_car.goto(start_x, start_y)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        self.cars.append(new_car)

    def generate_cars_start(self, n):
        for _ in range(n):
            start_x = random.choice(STEPS_X)
            self.make_car(start_x)

    def move_car(self):
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor()<-MAX_X:
                self.delete_car()

    def generate_new_car(self):
        self.count += 1
        if self.count == 6:
            self.make_car(MAX_X)
            self.count = 0
    def delete_car(self):
        pass

    def speed_up(self):
        self.move_speed+=MOVE_INCREMENT
