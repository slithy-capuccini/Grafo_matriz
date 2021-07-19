import numpy as np
from colorama import Fore

Matrix=[]
camino=[]
"""

lines = open('E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt','r')
for line in lines:
    line = line.split()
    Matrix.append(line)
#Matriz=np.loadtxt("E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt",dtype="int",delimiter=',')
Matriz= ( [list( map(int,i) ) for i in Matrix] )"""
Matriz=[[0,7,3,100,100],
       [7,0,2,7,8],
       [3,2,0,100,4],
       [100,7,100,0,9],
       [100,8,4,9,0]]
print(Matriz)

L_Dist=[]
