# soma = 0
# contador = 0

# while True:
#     numero = int(input("Digite um número (Digite 0 para sair): "))
#     if numero == 0:
#         break
#     soma += numero
#     contador += 1

# print(f"Soma dos numeros: {soma}\nQuantidade de numeros: {contador}")

contador = 0      # contador começa em 0
soma = 0          # acumulador começa em 0
numero = int(input('Digite um numero: '))  # primeira leitura

while numero != 0:
    soma += numero        # acumula
    contador += 1         # conta
    numero = int(input('Digite um numero: '))  # lê novamente

print(f'A soma dos numero é {soma}\nO contador é {contador}')