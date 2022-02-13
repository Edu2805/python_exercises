#strings
# imprimir na mesma linha


print('Eduardo','Amorim', sep='-', end=' ')
print('Eduard', 'Amorim')
# o sep='-'determina que voce possa fazer a separacao de duas strings
# por algum cacatere que vc escolher, neste caso um "-"
# o end='' faz com que o proximo print seja emitido na mesma linha
print()
# contar quantos caracteres tem em uma string
nome = 'Eduardo'
qtdCaractere = len(nome)
print(qtdCaractere)

#################################################
# Pass e Elipisis
# usado, geralmente dentro de uma condicional, ele "pula" a condicional
# se o Pass ou elipsis estiver dentro da condicional True, ele pula
# usado para situacoes em que o dev ainda nao decidiu o que executar
# caso a condição der true, entao ele preenche este espaço para nao dar erro

#usando o pass
valor = True

if valor:
    pass
else:
    print("Tchau!")

# usando Elipsis
if valor:
    ...
else:
    print("Tchau!")

#################################################
#Maneiras de inserir dados pelo input

#1 - Já sinalizando o tipo de entrada
x = int(input("Digite um numero inteiro: "))
y = float(input("Digite um numero real: "))
nome = input("Digite o seu nome: ")
# no caso acima existe um problema que, caso o usuário digitar um
# numero real no lugar do inteiro, o programa para
# é um problema já determinar que tal numero será um inteiro ou real na entrada do usuário
# da para tratar esse erro

#Obs - caso o usuário digite um numero real no lugar do inteiro
# o programa vai retornar erro, se esse erro nao for tratado
# o programa para
# tratando o erro

#2 - Nao sinalizando o tipo de entrada, deixando genérico
z = input("Digite um numero: ")

# tratando um possivel erro e transformando o dado em inteiro
if z.isdigit():
    verificainteiro = int(z)
else:
    print("Digite um inteiro")

# formatação de valores
# controlando casas decimais

# pelo método tradicional usando placeholder '{:.2f}'
divisao = 10 / 3
print('{:.2f}'.format(divisao))
# usando fstimgs
print(f'{divisao:.2f}')

# outros placeholders:
# :s-> strings      |  > esquerda
# :d-> inteiros     |  < direita
# :f-> float        |  ^ centro

# adicionando dígitos a esquerda, direita e centro
# a esquerda

num_1 = 1
# adiciona 10 digitos (0) a esquerda, incluindo o numero 1
print(f'{num_1:0>10}')

# adiciona 10 digitos (0) a direita, incluindo o numero 1
print(f'{num_1:0<10}')

# adiciona 10 digitos (0) no centro, incluindo o numero 1
# Obs: neste caso o 1 nao fica exatamente no meio, pois 10 é par
print(f'{num_1:0^10}')

# adicionando a esquerda com casas decimais
print(f'{num_1:0>10.2f}')

# adicionando caracteres e deixando um string no meio
nome = 'Eduardo Amorim'
print(f'{nome:#^50}')

# adicionando caracteres a esqueda da string
print(f'{nome:#>50}')

# adicionando caracteres a direita da string
print(f'{nome:#<50}')

# acessando um caractere específico em uma string
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])

# Outras utilidades
# imprimir uma string com as letras iniciais em minusculo
print(nome.lower())

# imprmir uma string com as letras iniciais em minúsculo
sobrenome = 'amorim'
print(sobrenome.title())

#imprimir uma string com todas a letras maiúscula
sobrenome = 'amorim'
print(sobrenome.upper())

# indices e fatiamento de strings
url = 'www.google.com.br/'
# removendo o último caractere de uma strings
print(url[:-1])

# exibindo caracteres em específico
texto = 'Python_S2'
#exibe os caracteres do indice 2 ao 6(6-1)
nova_string = texto[2:6]
print(nova_string)

# exibindo do índice 0 até o 6
nova_string2 = texto[:6]
print((nova_string2))

# exibindo do indice 7 até o final da string
nova_string3 = texto[7:]
print(nova_string3)

# exibindo o último caractere
nova_string3 = texto[-1]
print(nova_string3)

# exibindo o primeiro caractere
nova_string3 = texto[-9]
print(nova_string3)

# exibindo caracteres usando numeros negativos
nova_string3 = texto[-9:-3] # do primeiro ao quinto
print(nova_string3)

# retirando o último caractere
nova_string3 = texto[:-1]
print(nova_string3)

# pulando strings
#[0:]caractere inicial
#[0:6:] caractere final
#[0:6:2] determina quantos caracteres deseja pular
nova_string3 = texto[0:6:2]
print(nova_string3)

# Listas (vetores)
# também suporte as mesmas configuracoes para fatiamento
# unindo duas listas
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

# adicionando um elemento n0 fim da lista
l2.append("b")
print(l2)

# adicionando um elemento em um lugar específico da lista
l2.insert(0, 'banana')
print(l2)

# deletando um elemento (último elemento)
l2.pop()
print(l2)

# deletando elementos em específico
l3 = [1,2,3,4,5,6,7,8,9]
del (l3[3:5]) # deletou do tres ao cinco
print(l3)

# inserindo valores de forma automática
# determina o range que vc quer inserir
l3 = list(range(1,10))
print(l3)

