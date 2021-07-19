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
Matriz=[[0,110,25,30,65], 
[110,0,166,123,160],
[25,166,0,35,47],
[30,123,35,0,142],
[65,160,47,142,0]]
L_Dist=[]
L_nodesauxiliares=[]
L_segui=[]
print(Matriz)
node_inicio=int(input("Introduce la ciudad de inicio(y de final):"))
node_start=node_inicio
if node_inicio>5:
    print("Enter a num between 90 and 4")
L_nodesauxiliares.append(node_inicio)
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
total=0
while len(L_nodesauxiliares)!=len(Matriz[node_inicio]):
    L_Dist.clear()
    for i in range(len(Matriz[node_inicio])):
        L_Dist.append(Matriz[node_inicio][i])
    minimo2=minima(L_Dist)
    print(L_Dist)
    print(minimo2)
    for x,i in enumerate(L_Dist):
        if x==minimo2:
            minimo=i
            total+=minimo
            L_nodesauxiliares.append(x)
    node_inicio=L_nodesauxiliares[-1]
L_nodesauxiliares.append(node_start)
total+=L_Dist[node_start]
print(Fore.GREEN+'El camino es',L_nodesauxiliares)
print(Fore.RED,'El resultado es',total,Fore.WHITE)