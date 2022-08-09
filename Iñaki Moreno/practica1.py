import random
lista=[]

for i in range (20):
    lista.append(random.randint(15,60))


for x in range(0,len(lista)):
    print(lista[x],end="     ")

print("\n")

print("fin")