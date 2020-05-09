from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import numpy as np
import time
import ipyturtle as turtle

seq=[220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744,10856,12285,14595,17296,18416,63020,76084,66928,66992,67095,71145,69615,87633,79750,88730,100485,124155,122265,139815,122368,123152,141664,153176,142310,168730,171856,176336,176272,180848,185368,203432,196724,202444,280540,365084,308620,389924,319550,430402,356408,399592,437456,455344,469028,486178,503056,514736,522405,525915,600392,669688,609928,686072,624184,691256,635624,712216,643336,652664,667964,783556,726104,796696,802725,863835,879712,901424,898216,980984,947835,1125765,998104,1043096]
ratio=[seq[i]/seq[i-1] for i in range(1,len(seq))]
angle=360/np.mean(ratio)**2
N=300

##########################################

def initCanvas(N=300):
    return turtle.Turtle(fixed=False, width=N, height=N)

def setInitPos(t,rY=N,rX=N):
    t.hideturtle()
    t.penup()
    t.back(N/rY)
    t.right(90)
    t.forward(N/rX)
    t.left(90)
    t.pendown()
    return t

def draw(indexMax=10,timewait=0.001):
    global angle
    for i in range(indexMax):
        for j in range(int(angle)): 
            t.forward(i/10) 
            t.left(1)
            if(i>15):
                time.sleep(timewait) # Чтобы не терять рисунок

if(__name__=="__main__"):
    N=int(input("type size of window "))
    while True:
        indexMax=int(input("indexMax "))
        if(indexMax < 50):
            break
    t=initCanvas(N)
    t=setInitPos(t)
    t
    draw(indexMax=indexMax)