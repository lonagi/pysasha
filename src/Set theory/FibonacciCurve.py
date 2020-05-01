from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def IterationFibonacciWord(index):
    Sn_1 = "0"
    Sn = "01"
    tmp = "" 
    for i in range(2, index + 1): 
        tmp = Sn
        Sn += Sn_1 
        Sn_1 = tmp 
    return Sn 
##########################################

def initCanvas(N=600):
    return turtle.Turtle(fixed=False, width=N, height=N)

def setInitPos(t,rY=2.2,rX=2.2):
    t.hideturtle()
    t.penup()
    t.back(N/rY)
    t.right(90)
    t.forward(N/rX)
    t.left(90)
    t.pendown()
    return t

def draw(indexMax=10,step=2,directionLeft=True,timewait=0.01):
    j=0
    k=0
    while j<indexMax:
        if(k==0):
            myword='0'
        else:
            myword=IterationFibonacciWord(j)
        for i in myword:
            t.forward(step)
            if(i=='0'):
                if((directionLeft and k%2!=0) or (not directionLeft and k%2==0)):
                    t.left(90)
                else:
                    t.right(90)
            k+=1
        j+=1
        time.sleep(timewait)

if(__name__=="__main__"):
    N=int(input("type size of window "))
    while True:
        indexMax=int(input("indexMax "))
        if(indexMax < 50):
            break
    step=int(input("step "))
    t=initCanvas(N)
    t=setInitPos(t)
    t
    draw(indexMax=indexMax,step=step)