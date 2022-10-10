import turtle
import time
import random

delay=0.1
queue=[]

pen=turtle.Turtle()
pen.shape('square')
pen.penup()
pen.speed()
pen.color('white')

pen.hideturtle()
pen.goto(0,210)
pen.write("Score : 0 High Score: 0", align='center', font=('Arial',25,'bold') )

#window
window=turtle.Screen()
window.bgcolor('black')
window.title('Snake game by Rawat')
window.setup(width=600,height=500)
window.tracer(0)

#snk_head
snk_head=turtle.Turtle()
snk_head.speed(0)
snk_head.shape('circle')
snk_head.color('cyan')
snk_head.penup()
snk_head.goto(0,0)
snk_head.direction='stop'

#snk_food
snk_food=turtle.Turtle()
snk_food.speed(0)
snk_food.shape('turtle')
snk_food.color('red')
snk_food.penup()
snk_food.goto(0,150)

def move():
    if snk_head.direction=='up':
        y=snk_head.ycor()
        snk_head.sety(y+10)

    if snk_head.direction=='down':
        y=snk_head.ycor()
        snk_head.sety(y-10)

    if snk_head.direction=='left':
        x=snk_head.xcor()
        snk_head.setx(x-10)

    if snk_head.direction=='right':
        x=snk_head.xcor()
        snk_head.setx(x+10)

def go_up():
    snk_head.direction='up'

def go_down():
    snk_head.direction='down'

def go_left():
    snk_head.direction='left'

def go_right():
    snk_head.direction='right'

def food_coll():
    if snk_head.distance(snk_food)< 15:
        snk_food.goto(random.randint(-290,290),random.randint(-249,249))
        snk_body=turtle.Turtle()
        snk_body.speed(0)
        snk_body.shape('circle')
        snk_body.penup()
        snk_body.color('blue')
        queue.append(snk_body)
        return True
    return False

def border_coll():
    if snk_head.xcor() >  290 or snk_head.xcor() < -290 or snk_head.ycor() > 249 or snk_head.ycor() <-249:
        time.sleep(1)
        snk_head.goto(0,0)
        snk_head.direction='stop'
        for segment in queue:
            segment.goto(1000,1000)
        queue.clear()
        return True

def body_coll():
    for segment in queue:
        if segment.distance(snk_head)< 10:
            time.sleep(1)
            snk_head.goto(0,0)
            snk_head.direction='stop'
            for segment in queue:
                segment.goto(1000,1000)
            queue.clear()
            return True
    return False

def add_snk_body():
    for i in range(len(queue)-1,0,-1):
        if i % 5==0:
            queue[i].goto(queue[i-1].xcor(),queue[i-1].ycor())
            queue[i].color('green')
            continue
        queue[i].goto(queue[i-1].xcor(),queue[i-1].ycor())
    if len(queue)>0:
        queue[0].goto(snk_head.xcor(),snk_head.ycor())

window.listen()
window.onkeypress(go_up,'Up')
window.onkeypress(go_down,'Down')
window.onkeypress(go_left,'Left')
window.onkeypress(go_right,'Right')

score=0
high_score=0
while True:
    window.update()
    move()
    if food_coll():
        score+=10
        high_score+=10
        if score> high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align='center',font=('arial',25,'bold'))

    if body_coll() or border_coll():
        score=0
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align='center', font=('arial',25,'bold'))
    time.sleep(delay)
    add_snk_body()

window.mainloop()

        
