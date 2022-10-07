
from vpython import * 
size = 0.2
h = 0.1
g = vector(0,-9.8,0)
my_window = canvas(
                title='3D長方體',
                width='900',
                height='600',
                backgroud=vec(0,0,0)
                ) 
floor = box(
            pos=vector(0,0,0),
            length = 20,
            height = h,
            width = 2,
            opacity = 0.6,
            canvas=my_window
            ) 
ball = sphere(
            color=color.red,
            radius=size,
            make_trail = True
            )
ball.pos = vector(-10+size,10,0)
ball.v = vector(1,0,0)
dt = 0.001

t = 0
i = 0
v_tmp = 0
pos_tmp = 0

while t <15:
    rate(1000)
    t = t + dt
    ball.v = ball.v + g*dt
    ball.pos = ball.pos + ball.v*dt

    if ball.v.y < 0 and v_tmp>0 :
        print("高度",ball.pos.y,"時間等於=",t)
    v_tmp = ball.v.y
    pos_tmp = ball.pos
    

    if ball.pos.y <= size+(h/2):
        ball.pos.y = size+h/2
        ball.v.y = -0.8*ball.v.y

    

