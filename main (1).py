#4: Crie um conjunto chamado "frutas" com as seguintes frutas: maçã, banana, laranja, pêra e abacaxi. Em seguida, imprima o número de elementos no conjunto.

frutas = 'maçã', 'banana', 'laranja', 'pêra', 'abacaxi'
print(len(frutas))

#5: Crie dois conjuntos, "conjunto1" e "conjunto2", com alguns números inteiros. Imprima a união desses dois conjuntos

conjunto1 = {3,5,8,7,10}
conjunto2 = {3,2,1,84,7}
uniao = conjunto1.union(conjunto2)
print(uniao)

#6: Dado o conjunto "cores" com cores diferentes, remova a cor "vermelho" do conjunto.

cores = {'vermelho', 'amarelo', 'azul', 'preto'}
cores.remove('vermelho')
print(cores)

#7: Verifique se o conjunto "alunos_aprovados" contém todos os alunos do conjunto "todos_alunos". Os conjuntos devem ser definidos com nomes apropriados.

todos_alunos = {'Thiago', 'Pedro', 'Joao', 'Maria'}
alunos_aprovados = {'Thiago', 'Maria'}
print(todos_alunos.intersection(alunos_aprovados))







#**A diferença entre dois conjuntos:**

conjunto1 = {2,3,6,5,9}
conjunto2 = {10,7,6,987}

##Verificando a existência de elementos:

if 3 in conjunto1:
  print('Está no conjunto 1')

print(conjunto1.difference(conjunto2))
print(conjunto2.difference(conjunto1))

##Adicionando elementos:

conjunto1.add(85)
conjunto2.add(21)

print(conjunto2)
print(conjunto1)

##Removendo elementos:

conjunto1.remove(3)
conjunto2.remove(987)

print(conjunto2)
print(conjunto1)

##Tamanho de um conjunto:

v = len(conjunto1)
v = conjunto2.intersection(conjunto1)
print(v)

for n in conjunto1:
  print(n)

# #1 - Crie uma função lambda que retorne o dobro de um número.

dobro = lambda x: x * 2
print(dobro(10))

# #2 - Crie uma função lambda que calcule a soma de dois números.

numeros = [6,10]
soma = lambda x,y: x + y
print(soma(numeros[0],numeros[1]))

# #3 - Crie uma função lambda que verifique se um número é par.

a= int(input('Digite um número: '))
par = lambda x: x % 2 == 0
par(a)

if par(a) is True:
    print('É par')
else:
  print('Não é par')

# #4 - Crie uma função lambda que converta uma string em maiúsculas.

maiuscula = lambda x: x.upper()
print(maiuscula('thiago'))

# #5 - Crie uma função lambda que calcule o produto de três números.

produto = lambda x,y,z: x * y * z
print(produto(8,5,10))


# # Exemplo com reduce():

# from functools import reduce

# numeros = [1, 2, 3, 4, 5]
# soma = reduce(lambda x, y: x + y, numeros)
# print(soma)  # Saída: 15


# # Exemplo com filter():

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)   # Saída: [2, 4, 6, 8, 10]



# # Exemplo com map():

# numeros = [1, 2, 3, 4, 5]
# n = [12,32]
# quadrados = list(map(lambda x: x ** 2, n))
# print(quadrados)  # Saída: [1, 4, 9, 16, 25]


