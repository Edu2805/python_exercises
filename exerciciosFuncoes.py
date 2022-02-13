def saudacoes (nome, saudacao):
    print(f"{saudacao} {nome}.")

saudacoes('Eduardo', 'Bem-vindo')

def soma (n1, n2, n3):
    print(n1+n2+n3)

soma(4,4,4)

def percentual(n1, percentual):
    return ((percentual / 100) + 1) * n1

resultado  = percentual(100, 10)
print(round(resultado,2))

def divisivel(numero):
    if numero % 2 == 0:
        return "fizz"

    elif numero % 5 == 0 and numero % 3 == 0:
        return "Fizzbuzz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero

conclusao = divisivel(27)
print(conclusao)
