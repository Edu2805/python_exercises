# tupa se declara com ou sem parenteses e não podem ser alteradas
# pode receber diversos tipos valores
# similar a listas

t1 = () # aqui ja temos uma tupla
print(type(t1))

# adicionando valores

t2 = (1,2,3,'a','Luiz Otávio')

for v in t2:
    print(v)

# fatiar tuplas
print(t2[2:]) # do elemento 2 até o último

# criar sem os parenteses

t3 = 1,2,3,'a','b'
print(t3)

# tupla com um elemento
# tem que adicionar a virgula, se não é só um inteiro
t4 = 1,

print(t4)
print(type(t4))

# concatenar tuplas

t5 = 1,2,'Luiz',4,5
t6 = 6,7,8,9,10

t7 = t5 + t6

print(t7)

# desempacotar en variáveis
# pega os tres primeiros elementos mais o resto
# faz o desempacotamento em uma variável
# no print vc escolhe qual elemento quer
n1, n2, n3, *_ = t7
print(n2) # elemento em específico desempacotado
print(*_) # resto da tupla

# neste caso, após o esterístico, ele vai pegar o último elemento

n1, n2, n3, *_, n10 = t7
print(n10) # último elemento desempacotado

# repetir uma tupla com multiplicador
# repete 20 x
t8 = (1,2,'Luiz',4,5) * 20
print(t8)

# convertendo tuplas em lista para edicao

t9 = (1,2,3,4,5)
# usar o list para converter para um lista
t9 = list(t9)
#agora sim, convertida para lista, da para fazer alteracoes
t9[1] = 3000

print(t9)
print(type(t9))

# converter novamente para tupla
t9 = tuple(t9)
print(type(t9))
print(t9)

