import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

# Solicitando los datos de entrado como son el radio y la altura del cono, usando la funcion input

radio = float(input("Ingrese el radio de la base del cono: "))
altura = float(input("Ingrese la altura del cono: "))

#Calculando el volumen del cono
volumen = (1/3)*math.pi*pow(radio,2)*altura

#Creando la figura y los ejes 

fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')

# Creando las mallas o grids para la supreficie lateral del cono

theta = np.linspace(0, 2*np.pi, 100)

g = np.linspace(0, radio, 50)

T,R = np.meshgrid(theta, g)

#Convirtiendo coordenadas polares a catesianas
X = R*np.cos(T)
Y = R*np.sin(T)

#Calculando la altura Z de cada punto de la superficie

Z = (altura/radio)*(radio - R)

ax.plot_surface(X, Y, Z, color= 'lightblue', alpha = 0.7)

#Graficando la linea de altura y radio

ax.plot([0,0],[0,0],[0, altura], color = 'blue', linestyle = '-', linewidth = 2, label = 'Radio (r)')

ax.plot([0,radio],[0,0],[0,0], color = 'blue', linestyle = '--', linewidth = 2, label = 'Altura (h)')

#Mostrando el volumen en el grafico

ax.text(0,0,altura +1, f'Vol = {volumen:.2f}m3', color = 'purple', fontsize = 12, ha = 'center')

#Mostrando kas dimensiones
ax.text(radio/2, 0, -1, f'r = {radio:.1f}m', color = 'blue')

ax.text(0, 0, altura/2, f'h = {altura:.1f}m', color = 'blue')

# Ajustar los limites de los ejes
ax.set_xlim(-radio, radio)
ax.set_ylim(-radio, radio)
ax.set_zlim(0, altura + 1)

#Agregando los label y el titulo
ax.set_xlabel('EJE X')
ax.set_ylabel('EJE Y')
ax.set_zlabel('EJE Z')
plt.title('CALCULANDO EL VOLUMEN DEL CONO', bbox = dict(facecolor = 'green', alpha = 0.5, edgecolor ='black', boxstyle ="round, pad = 0.5"), color = 'purple', fontsize= 14)

plt.legend()

plt.show()

