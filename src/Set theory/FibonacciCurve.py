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

def initCanvas():
	t = turtle.Turtle(fixed=False, width=N, height=N)
	return t

def setInitPos(rY=2.2,rX=2.2):
	t.hideturtle()
	t.penup()
	t.back(N/rY)
	t.right(90)
	t.forward(N/rX)
	t.left(90)
	t.pendown()

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

def main():
	N=int(input("type size of window"))
	initCanvas()
	setInitPos()
	draw()

if(__name__=="__main__"):
	main()