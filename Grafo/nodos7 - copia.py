import numpy as np 
from colorama import Fore
"""Matriz=[[0,7,3,100,100],
       [7,0,2,7,8],
       [3,2,0,100,4],
       [100,6,100,0,9],
       [100,8,4,9,0]]"""
Matrix=[]
cont=0
append_text='['
end_text=']'
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
contador3=0
L_Dist=[]
L_nodesauxiliares=[]
L_segui=[]
primero_val=0
segundo_val=0
L_Distmin=[]
L_Recprim=[]
node_inicio=int(input("Introduce el nodo de inicio:"))
node_final=int(input("Introduce el nodo final:"))
if node_inicio>5 or node_final>5:
       print("Enter a num between 0 and 4")
L_nodesauxiliares.append(node_inicio)
simple_result=Matriz[node_inicio][node_final]
listilla2=[]
cont5=0
def minima(lista):
    minimo=-1
    pos=0
    for x,i in enumerate(lista):      
        if i<minimo or minimo==-1:
            if x not in L_nodesauxiliares:
                minimo=i
                pos=x
    return pos
for i in range(len(Matriz[node_inicio])):
    L_Dist.append(Matriz[node_inicio][i])
    L_segui.append(node_inicio)
L_segui[node_inicio]=-1
def primero():
    cont2=0
    seguida=0
    while cont2<4:
        minimo2=minima(L_Dist)
        for x,i in enumerate(L_Dist):
            if x==minimo2:
                minimo=i
                L_nodesauxiliares.append(x)
        print(minimo2)
        cont2+=1
        for i in range(len(L_Dist)):
            if i not in L_nodesauxiliares:
                if L_Dist[i]>L_Dist[L_nodesauxiliares[-1]]+Matriz[L_nodesauxiliares[-1]][i]:
                    L_Dist[i]=L_Dist[L_nodesauxiliares[-1]]+Matriz[L_nodesauxiliares[-1]][i]
                    L_segui[i]=L_nodesauxiliares[-1]
        node_inicio=L_nodesauxiliares[-1]
        print("Lista nodos auxiliares:",L_nodesauxiliares)
        if node_inicio==node_final:
            cont2+=5
    seguida=node_final
    camino.append(seguida)
    Verdad=True
    while Verdad:
        if L_segui[seguida]==-1:
            Verdad=False
        else:
            camino.insert(0,L_segui[seguida])
            seguida=L_segui[seguida]
    print(Fore.GREEN+'El camino es',camino)
    L_Recprim=camino.copy()
    print('El resultado es',L_Dist[node_final],Fore.WHITE)
    return L_Recprim
a=primero()

def segundo(node_inicio):
    L_Dist_final=[100,100,100,100,100,100]
    for n in range(len(a)-1):
        L_nodesauxiliares.clear()
        L_nodesauxiliares.append(node_inicio)
        camino.clear()
        Matriz2=Matriz.copy()
        i=a[n]
        Matriz2[node_inicio][a[n+1]]=100
        L_segui.clear()
        L_Dist.clear()
        for j in range(len(Matriz2[node_inicio])):
            L_Dist.append(Matriz2[node_inicio][j])
            L_segui.append(node_inicio)
        L_segui[node_inicio]=-1
        cont2=0
        seguida=0
        while cont2<4:
            minimo2=minima(L_Dist)
            for z,j in enumerate(L_Dist):
                if z==minimo2:
                    minimo=j
                    L_nodesauxiliares.append(z)
            print(minimo2)
            cont2+=1
            for j in range(len(L_Dist)):
                if j not in L_nodesauxiliares:
                    if L_Dist[j]>L_Dist[L_nodesauxiliares[-1]]+Matriz2[L_nodesauxiliares[-1]][j]:
                        L_Dist[j]=L_Dist[L_nodesauxiliares[-1]]+Matriz2[L_nodesauxiliares[-1]][j]
                        L_segui[j]=L_nodesauxiliares[-1]
            node_inicio2=L_nodesauxiliares[-1]
            print("Lista nodos auxiliares:",L_nodesauxiliares)
            if node_inicio2==node_final:
                cont2+=5
        seguida=node_final
        camino.append(seguida)
        Verdad=True
        print()
        while Verdad:
            if L_segui[seguida]==-1:
                Verdad=False
            else:
                camino.insert(0,L_segui[seguida])
                seguida=L_segui[seguida]
        if L_Dist_final[node_final]>L_Dist[node_final]:
            L_Dist_final=L_Dist.copy()
            camino_final=camino.copy()
            print(L_Dist_final,camino_final)
            print(Fore.RED,'El segundo camino es',camino_final)
            print('El resultado del segundo camino es',L_Dist_final[node_final],Fore.WHITE)
segundo(node_inicio)