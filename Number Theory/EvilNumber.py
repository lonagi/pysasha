#Find Evil numbers
import time

evils = []
i = 3
while True:
    if(sum(map(lambda x : 1 if '1' in x else 0, str(bin(i))[2:] ))  % 2 == 0):
        evils.append(i)
    try:
        from IPython.display import clear_output
    except:
        pass
    clear_output(wait=True)
    print(evils)
    i+=1
    time.sleep(0.1)
