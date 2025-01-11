def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um numero: "))
if pertence_fibonacci(numero):
    print(f"O numero {numero} pertence a sequência de Fibonacci.")
else:
    print(f"O numero {numero} não pertence à sequência de Fibonacci.")
