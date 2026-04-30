def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    return n1 / n2

def calcular(n1,n2,operação):
    if operação == "+":
         return somar(n1,n2)
    elif operação == "+":
        return subtrair(n1,n2)
    elif operação == "*":
        return multiplicar(n1,n2)
    elif operação == "/":
        return dividir(n1,n2)
    else:
        return "Operação inválida"