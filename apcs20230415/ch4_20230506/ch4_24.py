import turtle
def draw_square(aturtle):
    for i in range(1,5):
        aturtle.forward(100)
        aturtle.right(90)

scan = turtle.Turtle()
scan.shape("turtle")
scan.color("green")
draw_square(scan)

amy = turtle.Turtle()

amy.goto(0,30)
amy.shape("arrow")
amy.color('red')
amy.circle(60)
