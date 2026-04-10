soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0: # condição de parada
        break
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"Soma: {soma} | Quantidade: {contador} | Média: {media:.2f}")
else:
    print("Nenhum número foi digitado.")