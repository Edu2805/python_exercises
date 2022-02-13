#funcao normal
def func(arg, arg2):
    return arg * arg2

var = func(2,2)
print(var)

#lambda - funcoes anonimas

#armazenar em uma variavel
#usar a expressao lambda seguida dos parametros (x, y)
# depois passar o retorno
a = lambda x, y: x * y
print(a(2,2))


#ordenar a lista pelo preco
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort() # alterando a ordem da lista
#porem, existe mais de uma lista dentro da lista
print(lista)

#para ordenar, criar uma funcao que indica qual indice a lista vc quer ordenar
def func1(item):
    return item[1]

#dar o comando sort e passar o nome da funcao como key
lista.sort(key=func1)
print(lista) # a lista será impressa pegando o indice 1 da lista e ordenar

#ordenar decrescente
lista.sort(key=func1, reverse=True)
print(lista)

#Nao precica criar uma funcao só para ordenar, basta fazer na lambda

lista1 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# dentro do sort, passar a funcao lambda como key
# na funcao lambda passar o parametro item e no retorno indicar qual indice
lista1.sort(key=lambda item: item[1], reverse=True)
print(lista1)

# outra maneira de organizar a lista sorted
print(sorted(lista1, key=lambda i: i[1], reverse=True))
