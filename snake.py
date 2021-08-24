from turtle import Turtle
# from scoreboard import Scoreboard
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# n = 3
# m_score = Scoreboard()

class Snake:

    def __init__(self):
        self.n1= 3
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]


    def create_snake(self):
        for snake1 in STARTING_POSITION:
            self.add_in_list(snake1)
            # snakem1 = Turtle("square")
            # snakem1.penup()
            # snakem1.color("white")
            # snakem1.goto(x=X_POSITION[snake1], y=0)
            # # X_POSITION.append(X_POSITION[-1] - 20)
            # self.snake_list.append(snakem1)

    def add_in_list(self, snake1):
        snakem1 = Turtle("square")
        snakem1.penup()
        snakem1.color("white")
        snakem1.goto(snake1)

        # X_POSITION.append(X_POSITION[-1] - 20)
        self.snake_list.append(snakem1)


    def extend(self):
        self.add_in_list(self.snake_list[-1].position())

    def move(self):
        for snake_list1 in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_list1 - 1].xcor()
            new_y= self.snake_list[snake_list1 - 1].ycor()
            self.snake_list[snake_list1].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)