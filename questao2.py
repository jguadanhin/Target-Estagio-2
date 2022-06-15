#Calculando a sequência Fibonacci

n = int(input('Digite o número de termos que deseja calcular: '))
termo1 = 0
termo2 = 1
print(f'{termo1} > {termo2}', end='')
n2 = 3
while n2 <= n:
    termo3 = termo1+termo2
    print(f' > {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    n2 += 1
print(' > FIM!')

#Checando se o número digitado é um número Fibonacci ou não
termo3=0
termo1=1
termo2=1

if (n == 0 or n == 1):
    print("O número digitado é um número Fibonacci")
else:
    while termo3 < n:
        termo3 = termo1 + termo2
        termo2 = termo1
        termo1 = termo3
    if termo3 == n:
        print("O número digitado é um número Fibonacci")
    else:
        print("O número digitado NÃO é um número Fibonacci")
