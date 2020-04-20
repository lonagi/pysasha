#Ratio function of Betrothed numbers to the previous with the number 1

a = [48,75,140,195,1050,1575,1648,1925,2024,2295,5775, 6128,8892,9504,16587,20735,62744,75495,186615, 196664,199760,206504,219975,266000,309135,312620, 507759,526575,544784,549219,573560,587460,817479, 1000824,1057595,1081184]
c = []

b = 48
for i in a:
    c.append( i / b )
    b = i
    
#Graph of the ratio function of Betrothed numbers to the previous
def graphRatio(a,c,nnn=1):
    try:
        import matplotlib.pyplot as plt
    except:
        pass
    plt.figure(num=None, figsize=(25, 25), dpi=50, facecolor='w', edgecolor='k')
    plt.grid()
    plt.title("Ratio function of Betrothed numbers to the previous with the number "+str(nnn))
    plt.xlabel("Numbers")
    plt.ylabel("Ratio")
    plt.rcParams.update({'font.size': 40})
    plt.plot(a,c,color="red",linewidth=5)
    
#Graph of acceleration of function of Betrothed numbers
def graphDensity(a,nnn=1):
    try:
        import matplotlib.pyplot as plt
    except:
        pass
    plt.figure(num=None, figsize=(25, 25), dpi=50, facecolor='w', edgecolor='k')
    plt.grid()
    plt.title("Acceleration of function of Betrothed numbers "+str(nnn))
    plt.xlabel("Index")
    plt.ylabel("Number")
    plt.rcParams.update({'font.size': 40})
    plt.plot(range(len(a)),a,color="red",linewidth=5)

#graphRatio(a,c)
#graphDensity(a)