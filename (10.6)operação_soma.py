print("Aperte 'q' para sair.")

while True:
    
    num1 = input("Digite o primeiro número: ")
    if num1 == 'q':
        break

    try:
        num1 = int(num1)
    except ValueError:
        print('Por favor digite apenas números!')
        continue

    num2 = input("Digite o segundo número: ")
    if num1 == 'q':
        break

    try:
        num2 = int(num2)
    except ValueError:
        print('Por favor digite apenas números!')
        continue
    soma = num1 + num2
    print(soma)
