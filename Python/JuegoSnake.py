import turtle
import time
import random


delay = 0.1
body_segments = []
score = 0
high_score = 0

wn = turtle.Screen()
#Title
wn.title("Juego Snake")
#Windows size
wn.setup(width=600, height=600)
#Background color
wn.bgcolor("black")
 
#Head settings

#Turtle object
head = turtle.Turtle()
#speed
head.speed(0)
#shape
head.shape("square")
#color
head.color("red")
#no rastro
head.penup()
#center
head.goto(0,0)
#para hacer que el programa espere a que yo le de una direccion
head.direction = "stop"


#settings comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)
food.direction = "stop"


#Score
text = turtle.Turtle()
text.speed = (0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0 , 260)
text.write(f"Score 0         Score mas alto: 0", align="center", font=("Arial", 24))



def mov():
    if head.direction == "up":
        #almacenar valor actual de la cordenada Y
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        #almacenar valor actual de la cordenada Y
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        #almacenar valor actual de la cordenada Y
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == "left":
        #almacenar valor actual de la cordenada Y
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"    
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"



#conectar con teclado
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")



while True:
    wn.update()
     
    #colisiones con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.diretion = "stop"
        
        #Esconder segmentos:
        for segment in body_segments:
            segment.goto(1000,1000)
            
        #clean segments after the game reiniciate
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f"Score {score}         Score mas alto: {high_score}", align="center", font=("Arial", 24))
        

    #Colisiones head vs food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
        #new segment config
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orangered3")
        new_segment.penup()
        body_segments.append(new_segment)

    
        score += 10
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f"Score {score}         Score mas alto: {high_score}", align="center", font=("Arial", 24))
    
    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0 ,-1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor() 
        body_segments[0].goto(x,y)

    mov()

    #colisiones con el propio cuerpo
    for segment in  body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Esconder segmentos:
            for segment in body_segments:
                segment.goto(1000,1000)

            body_segments.clear()
            score = 0
            text.clear()
            text.write(f"Score {score}         Score mas alto: {high_score}", align="center", font=("Arial", 24))
            

    time.sleep(delay)

 


turtle.done()


