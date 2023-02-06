import random
t = []
p = []
# cria números aleatórios de 1 a 100
for num in range(1,101):
    num = random.randrange(1,101)
    t.append(num)
print(t)
# separa os pares
for c in t:
    if(c%2==0):
        p.append(c)
# transforma as listas em conjuntos para comparar
a = set(t)
b = set(p)
x = a - b
print(x)
# mostra quantos números pares e ímpares o código elabora
print(len(p))
print(len(x))
