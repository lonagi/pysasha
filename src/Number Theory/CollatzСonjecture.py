import time
import datetime as dt
import operator
import sys

file = "log/collatz_%s.log" % dt.datetime.now().strftime("%Y-%m-%d_%H-%M")
sys.stdout = open(file, 'w+')

timestamp_start = time.time()

class vewr244():
    def __init__(self, myNum):
        self.myNum = myNum
        self.allmaxes = dict()

_ColNum = 5
ColNum = vewr244(_ColNum)

def Collatz(x, i, maxp):
    try:
        i += 1
        if (x == 1):
            print("maxp = ", round(maxp), " i= ", i)
        elif(x==0):
            print("no for ", x)
            Collatz(x + 1, i, maxp)
        else:
            c = x % 2
            if (c == 0):
                x = x / 2
            else:
                x = 3 * x + 1
            if (x > maxp):
                maxp = x
                if(maxp in ColNum.allmaxes.keys()):
                    ColNum.allmaxes[maxp] += 1
                else:
                    ColNum.allmaxes[maxp] = 1
            print("x= ", round(x))
            Collatz(x, i, maxp)
    except:
        print("no for ", x)
        Collatz(x+1, i, maxp)

def tryPrin():
    try:
        ColNum.myNum = int(input())
        print(ColNum.myNum)
        Collatz(ColNum.myNum, 0, 0)
    except:
        print("Some error? code - 2")
        tryPrin()


print("type number")

try:
    tryPrin()
except:
    print("Some error? code - 1")
    tryPrin()

print("\n\n",ColNum.myNum)
for i in range(ColNum.myNum+1):
    print("\n-----%s-i -----" % i)
    Collatz(i,0,0)

print("\n -- FREC-S -- \n")
for i,j in sorted(ColNum.allmaxes.items(), key=lambda x:x[1]):
    print("for %s = %s raz" % (round(i),round(j)))
print("\n -- FREC-S2 -- \n")

print(time.time()-timestamp_start, " seconds")