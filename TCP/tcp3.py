##11>53
import numpy as np
from colorama import Fore
from collections import OrderedDict

Matrix=[]
camino=[]
"""

lines = open('E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt','r')
for line in lines:
    line = line.split()
    Matrix.append(line)
#Matriz=np.loadtxt("E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt",dtype="int",delimiter=',')
Matriz= ( [list( map(int,i) ) for i in Matrix] )"""
Matriz=[[0,110,25,30,65], 
[110,0,166,123,160],
[25,166,0,35,47],
[30,123,35,0,142],
[65,160,47,142,0]]
L_Dist=[]
L_nodesauxiliares=[]
L_Rec=[]
L_nodesauxiliares_final=[]
L_segui=[]
L_Vals=[]
print(Matriz)
node_inicio=int(input("Introduce la ciudad de inicio(y de final):"))
node_start=node_inicio
if node_inicio>5:
    print("Enter a num between 0 and 4")
def minima(lista):
    minimo=-1
    pos=0
    for x,i in enumerate(lista):      
        if i<minimo or minimo==-1:
            if x not in L_nodesauxiliares:
                minimo=i
                pos=x
    return pos
cont2=0
seguida=0
for i in range(len(Matriz[node_inicio])):
    L_Dist.append(Matriz[node_inicio][i])
total=0
L_nodesauxiliares_final=[]
L_nodesauxiliares_2=[]
L_Vals_2=[]
L_Vals_final=[]
"""Pasos:
-Recorrer todos los nodos desde el nodo inicio
-Desde el nodo seleccionado recorrer todos los nodos posibles 
-Asi sucesibamente
##bucle que recorra todas los sitios a los que se puede ir desde el node_inicio """

for x,i in enumerate(Matriz[node_inicio]): 
    L_nodesauxiliares.append(x)
    L_Vals.append(i)
    for x2,i2 in enumerate(Matriz[x]):
        if x2 not in L_nodesauxiliares:
            L_nodesauxiliares.append(x2)
            L_Vals.append(i2)
            for x3,i3 in enumerate(Matriz[x2]):
                if x3 not in L_nodesauxiliares:
                    L_nodesauxiliares.append(x3)
                    L_Vals.append(i3)
                    for x4,i4 in enumerate(Matriz[x3]):
                        if x4 not in L_nodesauxiliares:
                            L_nodesauxiliares.append(x4)
                            L_Vals.append(i4)
                            print(L_nodesauxiliares)
                            print(L_Vals)
                            L_nodesauxiliares.clear()
                            L_Vals.clear()
