def fibonacci(numero):
    fib_arr = [0, 1]
    n = 0
    soma = 0
    while numero >= soma:
        soma = fib_arr[0 + n] + fib_arr[1 + n]
        fib_arr.append(soma)
        n = n + 1
    print(fib_arr)
    return fib_arr

def checar_fibonacci(numero, fib):
    if fib.__contains__(numero):
        print("pertence a fibonacci")
        return
    print("não pertence a fibonacci")

numero = int(input())
checar_fibonacci(numero, 
                 fibonacci(numero))