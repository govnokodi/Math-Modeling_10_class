import numpy as np
import matplotlib.pyplot as plt

#1
plt.plot([1,1,5,5,1],[1,5,5,1,1])
plt.show()


#2
def func (x=1,a=1,b=1,c=1):
    """ функция которая создает 2 графика, по введенным параметрам
    x - неизвестная переменная, и коэффы - a,b,c
    синий график - параьола, красный - гипербола
    """
    plt.ioff()
    x = np.arange(-9, 10)
    y1 = a * x ** 2 + b * x + c
    xmin = -20
    xmax = 20
    dx = 0.1

    xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)

    ylist = 1 / xlist

    plt.plot(xlist, ylist)
    
    fig, ax = plt.subplots()
 
    ax.plot(x, y1, 'b', x, 'r--')

 
    lgnd = ax.legend(['y1 ', 'y2'], loc='upper center', shadow=True)
    lgnd.get_frame().set_facecolor('#ffb19a')
 
    plt.show()
func(15,13,15,81)


