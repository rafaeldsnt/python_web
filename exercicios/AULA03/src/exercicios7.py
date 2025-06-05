def seq_fibonacci(n):
    if n <= 1:
        return n
    return seq_fibonacci(n - 1) + seq_fibonacci(n - 2)

int_number = int(input("Informe o numero de termos da Fequencia de Fibonacci ...  "))
for i in range(int_number):
    print(seq_fibonacci(i), end=" ")