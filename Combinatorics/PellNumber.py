#Pell number
import time
Pells = [1,2,5]

i = 3
while True:
    num = Pells[i-1]*2 + Pells[i-2]
    Pells.append(num)
    i+=1
    time.sleep(0.1)
        
    try:
        from IPython.display import clear_output
    except:
        pass
    clear_output(wait=True)
    print(Pells)
