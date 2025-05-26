import matplotlib.pyplot as plt 
import numpy as np
theta = np.arange(0,2*np.pi, np.pi/360)
e_Io = 4.1*10**(-3)
e_Europa= 9.4*10**(-3)
e_Callisto = 1.1*10**(-3)
e_Ganimede = 7.4*10**(-3)

l_Io = 421700
l_Europa = 671100
l_Ganimede = 1070400
l_Callisto = 1882700

def polar(e,l,theta):
    r = l/(1-e*np.cos(theta))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

x_Io, y_Io = polar(e_Io, l_Io, theta)
x_Europa, y_Europa = polar(e_Europa, l_Europa, theta)
x_Ganimede, y_Ganimede = polar(e_Ganimede, l_Ganimede, theta)
x_Callisto, y_Callisto = polar(e_Callisto, l_Callisto, theta)

plt.figure(figsize=(10, 10))
plt.plot(x_Io, y_Io, label='Io')
plt.plot(x_Europa, y_Europa, label='Europa')
plt.plot(x_Ganimede, y_Ganimede, label='Ganimede')
plt.plot(x_Callisto, y_Callisto, label='Callisto')
plt.title("Orbite satelliti medicei")
plt.gca().set_aspect('equal', adjustable='box')  
plt.legend()
plt.show()

