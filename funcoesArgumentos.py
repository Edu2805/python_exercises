"""
Funcoes (def) em Python - *args **kwargs
"""

#argumento nomeado não ha a necessidade de passar na achamada da funcao
#caso tenha passado alguma argumento padrao, se for inserrir outros argumentos posteriormente, todos eles sao obrigados a serem nomeados
def func(a1, a2, a3, a4, a5, nome = None, a6 = None):
    print(a1, a2, a3, a4, a5, nome, a6)

# na chamada da funcao, apartir do momento que em que eu nomeio um argumento, os seguintes tbm terão que nomeados
func(1,2,3,4,5, nome = 'Luiz', a6 = "Carlos")
# caso queira armazenar esses valores em uma variável, terá que fazer o return dentro da funcao

def func2(a1, a2, a3, a4, a5, nome = None, a6 = None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6 # tupple

var = func2(1,2,3,4,5,nome = 'Luiz', a6 = '5')
print(var)
print(var[0], var[1])

# vao existir casos em que não vamos saber quantos argumentos serao passados para a funcao
# na impossibilidade de saber quantos valores serao passados, usa-se o *args
def func3(*args): # estão empacotados
    print(args)
    print(args[0]) # acessa o primeiro valor
    print(args[-1]) # acessa o último valor
    print(len(args)) # conta quantos elementos tem

func3(1,2,3,4,5) # estao empacotados

# dando um exemplo

lista = [1,2,3,4,5]
n1, n2, *n = lista # o *n vai retornar o resto da lista empacotada, o n1 e n2 estao desempacotados
print((n1, n2, n))

lista2 = [1,2,3,4,5]
print(lista2) # desta maneira será ixibida a lista empacotada
print(*lista2) # assim a lista será desempacotada
print(*lista2, sep="-") # separado por "-"

#tupples nao podem ser desempacotadas
def func4(*args):
    #args[0] = 20 #se tentar desempacotar vai retornar erro
    print(args)


func4(1,2,3,4,5)

def func5(*args):
    args = list(args) # fazer um casting transformando em uma lista
    args[0] = 20
    print(args)

func5(1,2,3,4,5)

def func6(*args):
    for v in args:
        print(v)

func6(1,2,3,4,5)

def func7(*args):
    print(args)

lista7 = [1,2,3,4,5]
#index  0     1    da tupple, exibe em índices separados
func7(lista, '6')
#realizando o desempacotamento, o 6 passa a integrar lista
func7(*lista7, '6')
lista8 = [6, 7, 8, 9, 10]
func7(*lista7, *lista8) # elementos da lista8 fazem parte da lista 7

# **kwargs - argumentos com palavras chaves

def func8(*args, **kwargs):
    print(args)
    #apresentar as palavras chaves para que possa exibir seus valores
    print(kwargs['nome'], kwargs['sobrenome'])

lista9 = [1,2,3,4,5]
lista10 = [6, 7, 8, 9, 10]
# caso não seja passada a palavra chave para kwargs, no caso nome e sobrenome
# não irá imprimir Luiz e Carlos
func8(*lista9, *lista10, nome='Luiz', sobrenome='Carlos')
