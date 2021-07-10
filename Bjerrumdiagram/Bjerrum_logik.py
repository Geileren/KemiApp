import matplotlib.pyplot as plt
import numpy as np
import sys



def createData(pk_a): #calculates datapoints at given pk_a
    pH = np.arange(pk_a - 3.5, pk_a + 3.5, 0.1)
    x_s = 1 / (np.exp(pH * np.log(10) - pk_a * np.log(10)) + 1)
    plt.plot(pH, x_s)

def draw_Graph(pk_a, h):
    for i in range(h):
        createData(pk_a[i])

    plt.xlabel("pH-værdi")
    plt.ylabel("x_s-værdi (andel i %)")

    plt.xlim(0,14)
    plt.ylim(0,1.0)

    plt.title("Bjerrumdiagram")
    plt.grid()
    plt.savefig(f"{sys.path[0]}\Bjerrumsaves\save.png")

    #plt.show() #shows img in IDE

def save(name):
    plt.savefig(f"{sys.path[0]}\Bjerrumsaves\{name}.png")

if __name__ == '__main__':
    draw_Graph([2.4,12.1], 2)
    plt.show()