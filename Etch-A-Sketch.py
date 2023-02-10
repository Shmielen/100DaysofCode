from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def mv_frwd():
    t.forward(10)

def mv_bck():
    t.backward(10)

def mv_lft():
    t.left(10)


def mv_rht():
    t.right(10)


def clr():
    t.clear()
    t.penup()
    t.home()
    t.pendown()




s.listen()
s.onkey(fun=mv_frwd, key="w")
s.onkey(fun=mv_bck, key="s")
s.onkey(fun=mv_lft, key="a")
s.onkey(fun=mv_rht, key="d")
s.onkey(fun=clr, key="c")
s.exitonclick()
