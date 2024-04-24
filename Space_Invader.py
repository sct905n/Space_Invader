import turtle
from random import randint
import math
import winsound


#khai báo màn hình 
screen = turtle.Screen()
screen.setup(800,500) 
screen.bgpic('space.gif')
screen.title('Space War')
screen.tracer(5)

#khai báo vùng di chuyển của các nhân vật
a = turtle.Turtle()
a.penup()
a.showturtle()
a.goto(-400,250)
a.pendown()
a.pensize(4)
a.pencolor('red')
a.speed(0)
a.hideturtle()
for i in range(0,2):
    a.forward(800)
    a.right(90)
    a.forward(500)
    a.right(90)





#khai báo nhân vật
nv = turtle.Turtle()
image = 'spaceship.gif'
screen.addshape(image) 
nv.shape(image) 
nv.penup()
nv.seth(90)
nv.goto(0,-200)

#khai báo độ thay đổi khi dùng phím
move_speed = 30

#tạo các hàm để nv di chuyển
def tien():
    y = nv.ycor()
    y += move_speed
    nv.sety(y)

def lui():
    y = nv.ycor()
    y -= move_speed
    nv.sety(y)

def right():
    x = nv.xcor()
    x += move_speed
    nv.setx(x)

def left():
    x = nv.xcor()
    x -= move_speed
    nv.setx(x)
    


#kiểm tra chạm khung
def chamkhung(i):
    if i.xcor() <- 400:
        i.setposition(375,i.ycor())

    if i.xcor() >400:
        i.setposition(-375, i.ycor())

    if i.ycor() > 250:
        i.setposition(i.xcor(), -225)

    if i.ycor() <-250:
        i.setposition(i.xcor(), 225)


#khai báo quái vật
so_luong_quai = 5
quaivat = []
image2 = 'monster.gif'
screen.addshape(image2)
for mons in range(so_luong_quai):
    mons = turtle.Turtle()
    mons.shape(image2)
    mons.penup()
    mons.speed(0)
    mons.setposition(randint(-390,390),randint(-240,240))
    quaivat.append(mons)

#kiểm tra va chạm
def collision(t1,t2):
    #d = nv.distance(mons)
    #d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    d = t1.distance(t2)
    if d < 20:
        return True
    
    else:
        return False

#khởi tạo đạn
dan = turtle.Turtle()
dan.shape('circle')
dan.shapesize(0.5,0.5,0.5)
dan.color('red')
dan.speed(0) #tốc độ khởi tạo đạn
dan.setheading(90)
dan.penup()
dan.hideturtle()
tocdodan = 8 #tốc độ đạn điều khiểu
trangthai = 'ready'



#tạo hàm để đạn có thể bắn
def ban_dan():
    global trangthai
    if trangthai == 'ready':
        trangthai = 'fire'
        winsound.PlaySound('lasersound.wav', winsound.SND_ASYNC)

        x = nv.xcor()
        y = nv.ycor() + 10
        dan.setposition(x,y)
        dan.showturtle()



screen.onkeypress(tien, 'Up')
screen.onkeypress(lui, 'Down')
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')
screen.onkeypress(ban_dan, 'space')
screen.listen() 

#vẽ khung điểm
score = 0
score_pen = turtle.Turtle()
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-380,210)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = 'left', font = ('Aria', 14, 'normal'))
score_pen.hideturtle()

highscore = 0 
#vẽ highscore
highscore_pen = turtle.Turtle()
highscore_pen.color('white')
highscore_pen.penup()
highscore_pen.goto(380, 210)
highscorestring = 'Highscore: %s' %highscore
highscore_pen.write(highscorestring, False, align = 'right', font = ('Arial', 14, 'normal'))
highscore_pen.hideturtle()


#xử lí highscore
f = open('highscore.txt', 'r', encoding = 'utf-8')
data = f.read()
f.close()
data1 = data.split('\n')
#print(data1)

data2 = []
for i in data1:
    data2.append(i.split())
    #print("current data2: " + str(data2))
del data2[-1]
#print(data2)

data3 = []
for j in data2:
    data3.append(j[-1])
    #print("current data3: " + str(data3))
    
data4 = []
for k in data3:
    data4.append(int(k))
    #print(str(data4))
data4.sort()
                

if data4 == []:
    highscore = 0

else:
    highscore = data4[-1]
    highscore_pen.clear()
    highscorestring = 'Highscore: %s' %highscore
    highscore_pen.write(highscorestring, False, align = 'right', font = ('Aria', 14 , 'normal'))

monsspeed = 2
    
run = True
while run:
    screen.update()
    #kiểm tra nv chạm khung
    chamkhung(nv)

    #xử lí đạn chạm biên
    if dan.ycor() > 250:
        dan.hideturtle()
        trangthai = 'ready'

    #đạn di chuyển
    if trangthai == 'fire':
        y = dan.ycor()
        y += tocdodan
        dan.sety(y)
            


    #=== xét các va chạm với quái
    for mons in quaivat:
        mons.forward(monsspeed)
        mons.left(randint(1,180))
        #kiểm tra quái chạm khung
        chamkhung(mons)

     


            

        #kiểm tra va chạm giữa đạn và quái
        if collision(dan,mons):
            dan.hideturtle()
            winsound.PlaySound('explosionsound.wav', winsound.SND_ASYNC)
            trangthai = 'ready'
            mons.hideturtle()
            mons.setposition(randint(-390,390), randint(-240,240))
            mons.showturtle()

            #thay đổi giá trị điểm số
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = 'left', font = ('Aria', 14, 'normal'))

            #xử lí highscore
            f = open('highscore.txt', 'r', encoding = 'utf-8')
            data = f.read()
            
            f.close()
            data1 = data.split('\n')

            data2 = []
            for i in data1:
                data2.append(i.split())         
            del data2[-1]

            data3 = []
            for j in data2:
                data3.append(j[-1])

            data4 = []
            for k in data3:
                data4.append(int(k))
            data4.sort()
                            

            if data4 == []:
                highscore = 0

            else:
                highscore = data4[-1]
                highscore_pen.clear()
                highscorestring = 'Highscore: %s' %highscore
                highscore_pen.write(highscorestring, False, align = 'right', font = ('Aria', 14 , 'normal'))

            #tạo hàm nếu người chơi phá kỷ lục
            def breakstreak():
                highscore_pen.clear()
                highscorestring = 'Highscore: %s' %score
                highscore_pen.write(highscorestring, False, align = 'right', font = ('Aria', 14, 'normal'))
            if highscore <= score:
                breakstreak()

        #if score >= 30:
            #monsspeed = 6

        #kiểm tra nv chạm quái
        if collision(nv,mons):
            mons.hideturtle()
            nv.hideturtle()
            winsound.PlaySound('oversound.wav', winsound.SND_ASYNC)
            print('GAME OVER!!')
            
            if highscore < score:
                print('!!! CHÚC MỪNG BẠN ĐÃ PHÁ KỶ LỤC !!!')
                
            tt_player = input('Nhập tên người chơi: ')
            info = 'Name: ' + tt_player.upper() +  ' Score: ' + str(score) + '\n'
            f = open('highscore.txt', 'a', encoding = 'utf-8')
            f.write(info)
            f.close()

            run = False

            
            
            
