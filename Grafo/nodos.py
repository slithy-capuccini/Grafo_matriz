from numpy import *

Matriz=[[0,7,3,20,20],
       [7,0,2,7,8],
       [3,2,0,20,4],
       [20,7,20,0,9],
       [20,8,4,9,0]]
L_Dist=[]
L_nodesauxiliares=[]
Vals_nodesauxiliares=[]
L_Distmin=[]
node_inicio=int(input("Introduce el nodo de inicio:"))
node_final=int(input("Introduce el nodo final:"))
if node_inicio>5 or node_final>5:
       print("Enter a num between 0 and 4")
L_nodesauxiliares.append(Matriz[node_inicio][node_inicio])

simple_result=Matriz[node_inicio][node_final]
contador=0
for i in range(len(Matriz[node_inicio])):
       L_Dist.append(Matriz[node_inicio][i])

print("Lista de distancias:",L_Dist)
minimo=min(x for x in L_Dist if x!=0 or x!=L_nodesauxiliares[x])
L_nodesauxiliares.append(L_Dist.index(minimo))
print("Lista de nodos auxiliares:",L_nodesauxiliares)
contador+=1
Vals_nodesauxiliares.append(Matriz[L_nodesauxiliares[contador]][node_final])
L_Dist.clear()
node_inicio=L_nodesauxiliares[contador]

for i in (Vals_nodesauxiliares):
    second_node=sum(i)
result=second_node+minimo
print(result)
if(result<simple_result):
    result=result
    print("El recorrido final es:",result)
    print("Pasando por el ", L_nodesauxiliares,"º nodo")
else:
    result=simple_result
    print("El recorrido final es:",result)
    print("Pasando por 0 nodos")
    