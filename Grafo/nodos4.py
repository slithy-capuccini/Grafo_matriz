import numpy as np 

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


lines = open('E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\Grafo\\matrix.txt','r')
for line in lines:
    line = line.split()
    Matrix.append(line)
#Matriz=np.loadtxt("E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt",dtype="int",delimiter=',')
Matriz= ( [list( map(int,i) ) for i in Matrix] )
print(Matriz)
contador3=0
L_Dist=[]
L_nodesauxiliares=[]
L_segui=[]
L_Distmin=[]
node_inicio=int(input("Introduce el nodo de inicio:"))
node_final=int(input("Introduce el nodo final:"))
if node_inicio>5 or node_final>5:
       print("Enter a num between 0 and 4")
L_nodesauxiliares.append(node_inicio)
simple_result=Matriz[node_inicio][node_final]
contador=0
cont2=0
contador3=0
lista2=[]
seguida=0
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
while cont2<4:
    print("Lista de distancias:",L_Dist)
    minimo2=minima(L_Dist)

    for x,i in enumerate(L_Dist):
        if x==minimo2:
            print(i,'es igual a minimo2')
            minimo=i
            L_nodesauxiliares.append(x)
    print("Lista de nodos auxiliares:",L_nodesauxiliares)
    cont2+=1
    for i in range(len(L_Dist)):
        if i not in L_nodesauxiliares:
            if L_Dist[i]>L_Dist[L_nodesauxiliares[-1]]+Matriz[L_nodesauxiliares[-1]][i]:
                L_Dist[i]=L_Dist[L_nodesauxiliares[-1]]+Matriz[L_nodesauxiliares[-1]][i]
                L_segui[i]=L_nodesauxiliares[-1]
    print('Lista seguimiento',L_segui)
    node_inicio=L_nodesauxiliares[-1]
    if node_inicio==node_final:
        cont2+=5
seguida==node_final
camino.append(seguida)
Verdad=True
while Verdad:
    if L_segui[seguida]==-1:
        Verdad=False
    else:
        camino.insert(0,L_segui[seguida])
        seguida=L_segui[seguida]
print('El camino es',camino)
print('El resultado es',L_Dist[node_final])