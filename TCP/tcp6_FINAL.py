##11>53
from typing import final
import numpy as np
import copy
from colorama import Fore
from collections import OrderedDict
import itertools
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
ways=[]
final_ways=[]
L_Vals_final=[]
Valores=[]
stuff=[0,1,2,3,4]
for permutation in itertools.permutations(stuff):
    permutation=list(permutation)
    permutation.append(node_inicio)
    ways.append(permutation)

for i in range(len(ways)):
    if ways[i][0]==node_inicio:
        final_ways.append(ways[i])
print(final_ways)

for j in range(len(final_ways)):
    for z in range(len(Matriz[node_inicio])):
        for x,i in enumerate(Matriz[node_inicio]):
            L_Vals.append(i)
        #print(L_Vals)
        L_Vals_final.append(L_Vals[final_ways[j][z+1]])
        node_inicio=final_ways[j][z+1]
        L_Vals.clear()
    print(L_Vals_final)  
    Valores.append(sum(L_Vals_final))  
    L_Vals_final.clear()
print(Valores)
minim=min(Valores)
print(minim)
num_minimo=Valores.index(minim)
print(final_ways[num_minimo])
