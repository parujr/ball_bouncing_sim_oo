import turtle

window = turtle.Screen()
window.setup(0.5, 0.75)
window.bgcolor(0, 0, 0)
window.title("My man")
player = turtle.Turtle()
player.color((1, 1, 1))

player = turtle.Turtle()
player.penup()
player.color(1, 1, 1)
player.shape("square")

class OfChange:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("My ")
        self.window.bgcolor(0, 0, 0)
        self.border = turtle.Turtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def draw_border(self):
        self.border.penup()
        self.border.goto(-20, -20)
        self.border.pensize(20)
        self.border.pendown()
        self.border.color((1, 1, 1))   
        for i in range(2):
            self.border.forward(50)
            self.border.left(90)
            self.border.forward(50)
            self.border.left(90)
        self.border.hideturtle()

# def move_forward():
#     while True:
#         turtle.penup()
#         turtle.setheading(90)
#         turtle.forward(50)

# def move_down():
#     turtle.penup()
#     turtle.setheading(-90)
#     turtle.forward(50)

# def move_left():
#     turtle.penup()
#     turtle.setheading(180)
#     turtle.forward(50)

# def move_right():
#     turtle.penup()
#     turtle.setheading(0)
#     turtle.forward(50)

# turtle.showturtle()

# turtle.onkey(move_forward, "Up")
# turtle.onkey(move_down, "Down")
# turtle.onkey(move_left, "Left")
# turtle.onkey(move_right, "Right")

turtle.listen()
turtle.done()