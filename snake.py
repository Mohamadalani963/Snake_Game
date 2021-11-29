from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0
class Snake():
    def __init__(self):
        self.segment = []
        self.createSnake()
        self.head = self.segment[0]

    # making the initial snake
    def createSnake(self):
        for position in starting_positions:
            self.addSegment(position)

    # function to make new piece of your snake
    def addSegment(self, position):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segment.append(segment_1)

    # function to extend the length of your snake
    def extends(self):
        self.addSegment(self.segment[-1].position())

    # snake moving function
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    # key pressing functions
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def right(self):
        if self.head.heading() != left:
          self.head.setheading(right)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def add(self):
        index = len(self.segment)
        x = self.segment[index-1]
        y = self.segment[index-1].ycor()
        z=0
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(x,y)
        self.segment.append(segment_1)

