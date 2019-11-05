import numpy as np
import matplotlib.pyplot as plt

#1
plt.plot([1,1,5,5,1],[1,5,5,1,1])
plt.xlim(-1,7)
plt.ylim(0,6)
plt.show()


#2 xmin=1,xmax=1,dx=1,
def func (a=1,b=1,c=0,k=1, title='Parabola + giperb'):
    """ функция которая создает 2 графика, по введенным параметрам
    x - неизвестная переменная, и коэффы - a,b,c
    синий график - параьола, красный - гипербола
    """  
    x = np.arange(-10,5,0.01)
    y1 = a*x**2 + b*x +c 
    plt.plot(x,y1, label='парабола')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    x = np.arange(0.01,4,0.01)
    y2 = k / x
    plt.plot(x,y2, label='гипербола')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
func()


#3
#def gg (R=1, width=1, height=4, cen=(1,-2)):
#    from matplotlib.patches import Ellipse
#    x = np.arange(-3, 3, 0.1)
#    y = np.arange(-3, 3, 0.1)
#    
#    X, Y = np.meshgrid(x,y)
#    fxy = X**2 + Y**2
#    plt.contour(X, Y, fxy, levels=[R])
#    
#    ax = plt.gca()
#    ellipse = Ellipse(cen, width, height, 
#                        edgecolor='r', fc='None', lw=2)    
#    ax.add_patch(ellipse)
#    
#    plt.xlim(-3,4)
#    plt.ylim(-3,2)
#    plt.show
#gg(3,4,2,(1,-1))

def gg1 (R=1, a=1, b=2):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    
    X, Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels=[R])
    
    fxy1 = (X**2/a**2)+(Y**2/b**2)
    plt.contour(X, Y, fxy1, levels=[2])
    plt.xlim(-7,8)
    plt.ylim(-6,5)
    plt.show
gg1(1,2,1)

