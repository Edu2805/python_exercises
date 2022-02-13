# escopos de variáveis

variavel = 'valor' # está em escopo global

def func():
    print(variavel) #visível dentro da funcao tbm

func()

def func2 ():
    # essa variável não tem nada a ver com a variável do escopo global, ou seja, o escopo dela é local
    # só está acessível nese escopo dessa funcao
    variavel = 'Outro valor'
    print(variavel)

func2()
print(variavel) # aqui o sistema pega o escopo global

# caso queira alterar uma variável de escopo de uma funcao,
# dentro da funcao basta colocar "Global" na frente da variavel
# porém não é uma boa prática

def func3():
    global variavel # agora o sistema altera a variável la do inicio
    variavel = 'Outro valor'
    print(variavel)

func3()

#uma maneira de alterar o valor da variável da funcao sem prejuízos

def func4(arg=None): # define o argumento como none
    arg = arg.replace('v', 'c')
    return arg #retorna o argumento

outra_variavel = func4(arg=variavel) # joga o valor em outra variável
func4(outra_variavel)

#conectando duas funcoes

def func5():
    outra_variavel1 = 'valor1' # cria a variável
    return outra_variavel1 # retorna o valor dela

def func6(arg): # cria uma segunda funcao com uma variável como argumento
    print(arg)

var = func5() # aqui a variável var recebe o retorno da func5
func6(var) # o resultado da var que recebe o retorno da funcao 5
# é passado como argumento na chamada da funcao func6