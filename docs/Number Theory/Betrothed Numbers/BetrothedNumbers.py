#!/usr/bin/env python
# coding: utf-8

# # Квази-дружественные числа. Исследование

# (или просто Обручённые числа)

# ### #Занимательная Математика
# 
# #### Весь код на Github, ссылка в конце статьи!

# Импорт библиотек

# In[1]:


from IPython.display import Image
from IPython.core.display import HTML 
from IPython.core.interactiveshell import InteractiveShell
from scipy.ndimage.filters import gaussian_filter1d
from scipy.signal import savgol_filter
import numpy as np
import sympy as sp
import pandas as pd
import random as r
import time
import matplotlib.pyplot as plt
import ipyturtle as turtle
#InteractiveShell.ast_node_interactivity = "all"

def drawPlot(ss,title="Скорости",y="Секунд",x="Номер итерации"):
    fig,ax=plt.subplots(figsize=(6,6))
    ax.set_facecolor("#F2F2F2")
    ax.grid()
    ax.set_title(title)
    ax.set_ylabel(y)
    ax.set_xlabel(x)
    ax.plot(ss)


# In[38]:


Image(url="https://sun9-27.userapi.com/5E-SgBD3vzq5A09aJ8lFJdeE-QVpBu397j9ZKg/pX1kJXlBs_E.jpg", width=400)


# Квази-дружественные числа это два положительных целых числа, для которых сумма собственных делителей каждого числа на 1 больше, чем второе число.  
# 
# Вот так вот они стоят рядом ☺  
# 
# Не имеют большого значения для теории чисел, однако являются интересным элементом занимательной математики. Что и есть интересно для нас :)

# In[3]:


def Divisors(num): 
    from math import sqrt as mmsq
    s=set([1])
    i=1
    a=int(mmsq(num)+1)
    while i<=a: 
        if(num//i==num):
            i+=1
            continue
        if (num%i==0): 
            if (num//i!=i): 
                s.add(num//i)
            s.add(i)
        i+=1
    return s


# In[4]:


Divisors(48)," #Делители числа 48"
Divisors(78)," #Делители числа 75"


# In[5]:


sum(Divisors(48))
sum(Divisors(75))


# И что мы наблюдаем? Сумма собственных делителей у 48 выдало нам 76, что на единицу больше, чем 75. А у 75 сумма выдала 49. Вот и элементарный пример!)

# И этот пример является первым представителем пар в множестве обручённых чисел!

# ## Факты

# 1) Все известные пары обручённых чисел имеют противоположную чётность.  
# 
# 2) Неизвестно, конечно или бесконечно количество пар обручённых чисел.  

# ## Алгоритмы 

# Первый алгоритм, который я решил сделать, это когда мы используем метод перебора. Простой брут форс.

# In[6]:


##Brute force Method
def BetrothedNumber(k,ratio=5.5,ratio2=5.5,order=1,returni=False):  
    ##All divisors for all numbers
    allDels=dict()
    
    ###Second number is greater than first number
    from itertools import chain
    concatenated = chain( range(k, int(k*ratio)+1 ),range(k, int(k/ratio2)+1 ,-1) )
    for i in concatenated:

        ###We don't want repeat operations
        ###Therefore search and save all divisors
        if(str(i) not in allDels):
            allDels[str(i)] = Divisors(i)

        ###Sum1+order_num = 2nd Num and Sum2+order_num = 1st Nub
        if(i != k and sum(allDels[str(i)]) == k+order and sum(allDels[str(k)]) == i+order):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)


# Особенность этого метода в том, что мы берём по порядку натуральное число, а затем в выбранном диапазоне перебираем числа в качестве пары.    
#   
# Каким образом я выбрал диапазон?  
# 
# Позже ещё расскажу

# In[7]:


BetrothedNumber(1) # Ничего
BetrothedNumber(48) # Нашли пару!


# Рассчитаем скорость выполнения данного алгоритма

# In[8]:


get_ipython().run_line_magic('time', 'BetrothedNumber(48)')


# In[9]:


get_ipython().run_cell_magic('timeit', 'BetrothedNumber(48)', ';')


# Такие вышли показатели для числа 48. Позже мы сравним с другим методом.   
# 
# Но можно также, построить график, чтобы узнать скорость

# In[10]:


s = np.array([])
for i in range(1,500):
    start_time = time.time()
    BetrothedNumber(i)
    end_time = (time.time() - start_time)
    s=np.append(s,end_time)


# In[11]:


drawPlot(s)


# Изначально я думал, что это алгоритм O(n), но он не так сильно усложняется со временем. Хотя смущает, что если мы нашли пару, то оно задерживается намного сильнее.

# Попробуем другой метод. Это тоже типо перебора, но здесь функция f(m,n), где мы подаём на вход два числа на проверку "квази-дружбы".

# In[12]:


def BetrothedNumbers(m,n,order=1):
    if(m!=n):
        s1=set([1])
        for i in range(int(m/2+1),1,-1):
            if(m%i==0):
                s1.add(i)
        s2=set([1])
        for i in range(int(n/2+1),1,-1):
            if(n%i==0):
                s2.add(i)
        return sum(s1)==n+1 and sum(s2)+n==sum(s1)+m
    else:
        return False


# In[13]:


BetrothedNumbers(48,75)


# In[14]:


get_ipython().run_line_magic('time', 'BetrothedNumbers(48,75)')


# In[15]:


get_ipython().run_cell_magic('timeit', '', 'BetrothedNumbers(48,75)')


# In[16]:


s = np.array([])
for i in range(1,100):
    start_time = time.time()
    for j in range(1,100):
        BetrothedNumber(i,j)
    end_time = (time.time() - start_time)
    s=np.append(s,end_time)


# In[17]:


drawPlot(s)


# Вот такие параметры выдал второй алгоритм. По этой причине, я выбираю первый брут форс!  
# 
# Если не понятно, то этот алгоритм дольше работает больше чем в 10 раз.

# Кстати, sympy снова нас подвёл. У него нет алгоритмов для квази-дружественных чисел, но зато я нашёл ещё алгоритм в Интернете. Попробуем разузнать, что с ним. 

# In[18]:


def NBetrothedNumbers(n) :
    bet=[]
    for num1 in range (1,n) : 
        sum1 = 1
        i = 2
        while i * i <= num1 : 
            if (num1 % i == 0) : 
                sum1 = sum1 + i 
                if (i * i != num1) : 
                    sum1 += num1 / i 
            i =i + 1
        if (sum1 > num1) : 
            num2 = sum1 - 1
            sum2 = 1
            j = 2
            while j * j <= num2 : 
                if (num2 % j == 0) : 
                    sum2 += j 
                    if (j * j != num2) : 
                        sum2 += num2 / j 
                j = j + 1
            if (sum2 == num1+1) : 
                bet.append ((num1,num2)) 
    return bet
n = 1000000
bet=NBetrothedNumbers(n) 
bet


# А он довольно быстрый! Быстрее, чем я мог написать!  
# Данная функция на вход принимает значение, до которого мы будем собирать пары

# Теперь мы можем ряд пар превратить в последовательный ряд чисел.

# In[19]:


flat_list = [item for sublist in bet for item in sublist]
flat_list


# Теперь покажу, почему стоит рассматривать следующие 5x чисел в диапазоне брутфорса.  

# In[20]:


df=pd.DataFrame([(48, 75.0), (140, 195.0), (1050, 1925.0), (1575, 1648.0), (2024, 2295.0), (5775, 6128.0), (8892, 16587.0), (9504, 20735.0), (62744, 75495.0), (186615, 206504.0), (196664, 219975.0), (199760, 309135.0), (266000, 507759.0), (312620, 549219.0), (526575, 544784.0), (573560, 817479.0), (587460, 1057595.0)])
df


# Итого я смог построить почти за 2 минуты 16 пар!

# Построим график того, как находится квази-друг по мере увеличениея входного значения в функцию.

# In[21]:


drawPlot(flat_list,y="Число")


# Попробуем посмотреть на таких данных какая будет скорость графика.

# In[22]:


dbet = [flat_list[i]-flat_list[i-1] for i in range(1,len(flat_list))]
drawPlot(dbet,title="Скорость обрученных чисел",x="Номер числа",y="Ускорение")


# Кстати, а по поводу отношений в 5.5 раз. Можем попробовать найти отношения среди этих 7 пар. Может есть сходимость?

# In[23]:


ratio=[flat_list[i]/flat_list[i-1] for i in range(1,len(flat_list))]
drawPlot(ratio,title="Отношения пар",x="Номер пары",y="Отношение")


# И вот мы видим два момента.  
# Первый: ряд не сходится

# Второй: если взять любое обручённое число и умножать его на любые числа до 5.5, то мы точно сможем найти его пару! Поэтому и получился своего рода диапазон.

# In[ ]:





# Узнаем среднее отношение

# In[24]:


np.mean(ratio)


# #### Плотность   
# По традиции, изучим плотность ряда квази-дружественных чисел!  
# А затем и скорость.

# In[25]:


densities=[(len(list(filter(lambda x: x < i, sorted(flat_list))))-1)/i for i in range(200,10000)]
drawPlot(densities,"Изменение плотности","Плотность","Обручённое число")


# Ого. Плотность стремительно идёт к нулю

# In[26]:


ddensities = [densities[i]-densities[i-1] for i in range(1,len(densities))]
drawPlot(ddensities,title="Скорость плотности",x="Обручённое число",y="Скорсоть")


# Кстати, а теперь если приглядется на линии, которые появились на графике скорости плотности, то мы поймём, что это точки перегиба!  
# 
# В целом, я бы сделал вывод, что раз плотность уменьшается, то находить обрученные числа с их ростом становится легче, если пренебречь тем, что числа большие.

# ### Статистика

# Узнаем сколько чётных и нечётных чисел в последовательности?

# In[27]:


InteractiveShell.ast_node_interactivity = "last"

EvenBetrothed=[i for i in flat_list if(i%2==0)]
len(EvenBetrothed)


# In[28]:


plt.pie([len(EvenBetrothed),34-len(EvenBetrothed)], 
        colors=["#A7FF5B","#E7AFFF"],
        labels=["Чётные","Нечётные"], 
        autopct='%1.1f%%',
        shadow=True,
        textprops={'color':"black"})
plt.legend([len(EvenBetrothed),34-len(EvenBetrothed)])
("")


# Идеальный баланс!

# Исследуем теперь на простоту!

# In[29]:


def _isPrime(n):
    if n%2==0:
        return n==2
    d=3
    while d*d<=n and n%d!=0:
        d+=2
    return d*d>n


# In[30]:


PrimeBetrothed=[(i) for i in flat_list if(_isPrime(int(i)))]
plt.pie([34-len(PrimeBetrothed),len(PrimeBetrothed)], 
        colors=["#A7FF5B","#E7AFFF"],
        labels=["Составные","Простые"], 
        autopct='%1.1f%%',
        shadow=True,
        textprops={'color':"black"})
plt.legend([34-len(PrimeBetrothed),len(PrimeBetrothed)])
("")


# Ни одного простого числа! Вот так забава.

# ### Фракталы

# Посмотрим, а можно ли нарисовать какие-то картинки по данному ряду?

# In[31]:


ratio=[flat_list[i]/flat_list[i-1] for i in range(1,len(flat_list))]


# $ угол={{2 \pi }\over{x^2}} $

# In[32]:


np.mean(ratio)


# In[33]:


angle=sp.N(360/np.mean(ratio)**2)
angle


# In[34]:


#Создаём картинку 300х300

N=300
t = turtle.Turtle(fixed=False, width=N, height=N)
t.hideturtle()
t


# In[35]:


for i in range(15):
    for j in range(int(angle)): 
        t.forward(i/10) 
        t.left(1)
        if(i>10):
            time.sleep(0.01) # Чтобы не терять рисунок


# In[36]:


t = turtle.Turtle(fixed=False, width=N, height=N)
t.hideturtle()
t


# In[37]:


for i in range(15):
    angle=sp.N(360/ratio[i]**2)
    for j in range(int(angle)): 
        t.forward(i/10) 
        t.left(1)
        if(i>10):
            time.sleep(0.04) # Чтобы не терять рисунок


# Если взять среднее соотношение чисел, то получается что-то типо рисунка компанейских чисел. (Не зря, существуют квази-компанейские числа)

# Но, как только у нас будет динамический угол, то получается расширенная версия дружественных чисел. Вроде и странная, а вроде и больше похожа на Google Chrome, чем было.

# ### Подведём итог

# Квази-дружественные (обрученные) числа имеют очень много похожих свойств с компанейскими и дружественными числами. И это удивляет. 

# # Конец  
# 
# На этом всё, дорогие читатели!  
# Надеюсь вам было интересно узнать что-то вроде такого из занимательной математики 😍
# 
# Прошлый раз я обещал расказать про совершенные числа, но у меня не хватает времени пока, что. Поэтому я успел сделать такую статью)
# Если у вас есть мысли или пожелания, обязательно напишите...Может найду что подправить или добавить.