import turtle as t

def draw_orange():
    t.penup()
    t.goto(-400, 350)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.fd(800)
    t.rt(90)
    t.fd(170)
    t.rt(90)
    t.fd(800)
    t.end_fill()
    t.color("white")
    t.begin_fill()
    t.lt(90)
    t.fd(170)
    t.end_fill()

def draw_green():
    t.color("green")
    t.begin_fill()
    t.fd(170)
    t.lt(90)
    t.fd(800)
    t.lt(90)
    t.fd(170)
    t.lt(90)
    t.fd(800)
    t.end_fill()
    t.bk(800)
    t.color("white")
    t.begin_fill()
    t.rt(90)
    t.fd(167)
    t.end_fill()

def draw_ashoka_chakra():
    t.penup()
    t.goto(18, 108)
    t.pendown()
    t.color("navy")
    t.pensize(10)
    t.circle(58)
    t.penup()
    t.goto(18, 100)
    for i in range(24):
        t.penup()
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.fd(15)
        t.left(15)
        t.pendown()
    t.color("navy")
    t.penup()
    t.goto(-40, 108)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.goto(-40, 108)
    t.pendown()
    t.pensize(3)
    for i in range(24):
        t.fd(45)
        t.bk(45)
        t.lt(15)

def draw_spokes():
    t.penup()
    t.goto(-40, 108)
    t.pendown()
    t.pensize(3)
    for i in range(24):
        t.fd(45)
        t.bk(45)
        t.lt(15)

def main():
    t.speed("fastest")
    t.setup(800, 650)
    draw_orange()
    draw_green()
    draw_ashoka_chakra()
    draw_spokes()
    t.done()

if __name__ == "__main__":
    main()