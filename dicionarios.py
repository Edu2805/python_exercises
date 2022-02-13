import copy
# quase a mesma coisa que lista
# em listas, o sistema cria um indice para vc
# no dicionário, voce cria os indices, chamados de chaves


# criando um dicoonário
# cria-se com {}, primeiro voce cria a chave(índice)
# após criar a chave, coloca-se os :
# depois vc insere o valor dessa chave entre ''

d1 = {'chave1':'valor da chave'}
# adionar novas chaves e valores
d1['nova_chave'] = 'Valor da nova chave'
# ou pode ser também com update()
d1.update({'mais_uma_chave':'novo_valor'})
print(d1)

# acessar uma chave específica
print(d1['chave1'])

# outra maneira de criar chave dict()
# formato anterior é mais usado
d2 = dict(chave1 = 'Valor da chave', chave2 = 'Valor dsa outra chave')
print(d2)

# as chaves não podem ter o mesmo nome

# chaves podem usar qualquer tipos de dados imutáveis, geralmente é usado para strings

d3 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}
# acessando chaves estranhas
print(d3[1,2,3,4]) # é uma chave válida

# excluir uma chave

print(d3)
# verificar se tal chave existe dentro do dicionário
print('str' in d3)
# ou
print('str' in d3.keys())

del d3['str']
print(d3)

# verificar se um valor existe dentro do dicionário
print('Tupla' in d3.values())

# saber quantos pares de chaves dentro do dicionário
print(len(d1))

# interar sobre os dicionários
print()
for k in d3:
    print(k) # só vai mostrar as chaves(indices)
print()

# para ver os valores
for v in d3.values():
    print(v)
print()

# mostrar chaves e valores
for k in d1.items():
    print(k)
    print(k[0], k[1]) # aqui ele acessa chave[0] e valor[1]

# desempacotar dicionários
for k, v in d3.items():
    print(k,v)

# discionário dentro de discionário
clientes = {
    'cliente1': {
        'nome' : 'Luiz',
        'sobrenome' : 'Otávio',
    },
    'cliente2': {
        'nome' : 'Joao',
        'sobrenome' : 'Moreira',
    },
}
# inteirando sobre o discionário
for cliente_k, clientes_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}, = {dados_v}')

# modificacoes nos valores
print()
dicionario1 = {1:'a', 2:'b', 3:'c'}
v = dicionario1
print(dicionario1)
print(v)
print()

# em tese era só para alterar o V, porém python intende que
# dicionario1 tbm seja alterada pois são identicos
# não se trata de um novo dicionário
v[1] = 'Luiz'
print(dicionario1)
print(v)

# gerar um cópia (cópia raza)

u = dicionario1.copy()
u[1] = "Carlos"
print(dicionario1)
print(u)

# uma lista como valor dentro de uma chave
dicionario2 = {1:'a', 2:'b', 3:'c', 'd':['Luiz', 'Otávio']}
x = dicionario2.copy()
# acessando a chave "d" que é uma lista, e dentro dessa chave
# indicar qual indice vc quer
#  ['chave'][indice]
print(x['d'][0])

# alterando valores (chalon copy)
# vai alterar nas duas listas
x ['d'][0] = 'Joãozinho'
print(dicionario2)
print(x)

# para criar uma cópia real de um dicionário, tem que
# usar um módulo chamado import copy
# com o modulo importado, ao inves de usar copy (cópia raza)
# pode usar copy.deepcopy() (copia profunda)

# agora torna os dicionários independentes um do outro
#dicionário 2 não será afetado pelas alteracoes de x
# não funciona para tupla
x = copy.deepcopy(dicionario2)
x ['d'][0] = 'Mariazinha'

print(dicionario2)
print(x)

# fazer casting na lista para dicionario dict()
# isso pode ser convertido para dicionario porque existe pares
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
# aqui é feita a conversao
d10 = dict(lista)
print(d10)

# fazer casting na tupla para dicionario dict()
# isso pode ser convertido para dicionario porque existe pares
lista1 = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
]
# aqui é feita a conversao
d11 = dict(lista)
print(d11)

#ou tuplas dentro de tuplas
lista2 = (
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
)
# aqui é feita a conversao
d12 = dict(lista)
print(d12)

#ou listas dentro de tuplas
lista3 = (
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
)
# aqui é feita a conversao
d13 = dict(lista)
print(d13)
print()
# eliminar chaves
lista4 = {
    1: 2,
    2: 3,
    4: 5,
}
#eliminando a chave 4 da lista
lista4.pop(4)
print(lista4)

#eliminar o último item
lista4.popitem()
print(lista4)

# concatenar dois dicionários
lista5 = {
    1: 2,
    2: 3,
    4: 5,
}

lista6 = {
    'a' : 'b',
    'c' : 'd',
}

lista5.update(lista6)
print(lista5)