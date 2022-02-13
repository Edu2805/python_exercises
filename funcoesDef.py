# Funcoes com Def

def saudacao(): #funcao normal
    print("Olá mundo!")

saudacao()

def saudacao2(msg,nome): # podem receber parametros
    print(msg,nome)

saudacao2("Olá", "Eduardo") # inserir os parametros
saudacao2("Oi", "José")
saudacao2("Hello", "Maria")

def saudacao3(msg="Hi", nome="Marcos"): # com parametros padroes
    print(msg, nome)

saudacao3() # capta os valores podroes
saudacao3("Bem-vindo", "Ricardo") # podem ser alterados também

# _______________________________
#Com retorno
# Funcoes com retono podem ser armazenadas em variáveis, sem retorno retornaria None

def funcao(var):
    return var

variavel = funcao('Valor que eu quero')
print(variavel)

def divisao(n1, n2):
    return n1 / n2

divide = divisao(8,2)
print(divide)



def divisao2(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide2 = divisao2(8,0) # na divisao, quando um valor é passado zero, o sistema vai retornar um erro, para tratá-lo basta fazer um if

if divide2: # se divide2 for True (retorna diferente de erro), ele faz a divisao
    print(divide2)
else: # caso retornar erro, exibe a menssagem
    print("Conta inválida")

def dumb():
    return 1

print(dumb(), type(dumb())) # verificar o tipo da funcao e retorno

# funcao chamando outra funcao

def f (var):
    print(var)

def a():
    return f

valor = a()
print(type(valor))
print(id(valor), id(f)) # mesma posicao na memoria

if valor == f:
    print('valor é igual a f')
else:
    print('Nao é igual')

valor('Imprime algo na tela') # é uma funcao tbm, pois recebe a

def nomes():
    return ('Luiz', 'Otávio')

var1 = nomes()
print(var1, type(var1)) # vai retornar o tipo "tuple", uma lista que nao pode ser alterada

# para acessar itens da lista
print(var1[0]) # vai acessar Luiz
print(var1[1]) # vai acessar Otávio
