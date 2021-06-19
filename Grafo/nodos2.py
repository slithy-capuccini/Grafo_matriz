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

#lines = open('E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt','r')

#for line in lines:
    #line = line.split()
    #Matrix.append(line)

#Matriz=np.loadtxt("E:\\Games\\1.LA CARPETA\\Programacion\\Jesus\\matrix.txt",dtype="int",delimiter=',')
#Matriz= ( [list( map(int,i) ) for i in Matrix] )
Matriz=[[0,7,3,100,100],
       [7,0,2,7,8],
       [3,2,0,100,4],
       [100,6,100,0,9],
       [100,8,4,9,0]]
print(Matriz)
L_Dist=[]
L_nodesauxiliares=[]
Vals_nodesauxiliares=[]
L_Distmin=[]
node_inicio=int(input("Introduce el nodo de inicio:"))
node_final=int(input("Introduce el nodo final:"))
if node_inicio>5 or node_final>5:
       print("Enter a num between 0 and 4")
L_nodesauxiliares.append(node_inicio)

simple_result=Matriz[node_inicio][node_final]
contador=0
cont2=0
minimo=0
while cont2<4:
    for i in range(len(Matriz[node_inicio])):
        L_Dist.append(Matriz[node_inicio][i])

    print("Lista de distancias:",L_Dist)

    minimo=min(x for x in L_Dist if x!=0 and L_Dist.index(x) not in L_nodesauxiliares)

    L_nodesauxiliares.append(L_Dist.index(minimo))
    print("Lista de nodos auxiliares:",L_nodesauxiliares)
    Vals_nodesauxiliares.append(Matriz[node_inicio][L_nodesauxiliares[-1]])
    contador+=1
    print("Lista valores nodesaxuliares:",Vals_nodesauxiliares)

    cont2+=1
    L_Dist.clear()
    node_inicio=L_nodesauxiliares[contador]
    if node_inicio==node_final:
        cont2+=5
second_node=sum(Vals_nodesauxiliares)
result=second_node
print(result)
if(result<simple_result):
    result=result
    print("El recorrido final es:",result)
    print("Pasando por el ", L_nodesauxiliares,"º nodo")
elif(result>=1000 or simple_result>=1000):
    print("IMPOSIBLE de ir a este nodo")
else:
    result=simple_result
    print("El recorrido final es:",result)
    print("Pasando por 0 nodos")
    