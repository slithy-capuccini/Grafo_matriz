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
L_Rec_final=[]
L_nodesauxiliares_2=[]
L_Vals_2=[]
L_Vals_final=[]
"""Pasos:
-Recorrer todos los nodos desde el nodo inicio
-Desde el nodo seleccionado recorrer todos los nodos posibles 
-Asi sucesibamente
##bucle que recorra todas los sitios a los que se puede ir desde el node_inicio 

TODO:
-Optimizar los for para que sea el len(nodos) = For y dentro un while 
-Usar concepto de djstrak
-Comprobar si es menor en vez de meter todos en una lista y cojer el menor
"""
def L_Dist(node=node_inicio):
    for x,i in enumerate(Matriz[node]):
        if x not in L_Rec:
            L_nodesauxiliares.append(x)
            L_Vals.append(i)
            L_Rec.append(x)
            #print(L_nodesauxiliares,L_Vals)
    return L_nodesauxiliares
def hola(node=node_inicio):
    l_dist=L_Dist(node)
    for x,i in enumerate(l_dist):
        node=L_Dist(x)
        print(node)
node=node_inicio
while len(L_Rec)!=len(Matriz[node_inicio]):
    if node==node_inicio:
        L_Dist() 
        hola()
    else:
        node=L_Dist(node)
        L_Dist(node)
        hola(node)
