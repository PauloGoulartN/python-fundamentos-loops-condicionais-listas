notas = []

while True:
    nota = float(input("Digite uma nota (Digite -1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)
if notas:
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
    print(f"Maior: {max(notas)}")
    print(f"Menor: {min(notas)}")
    print(f"Total de notas: {len(notas)}")
else:
    print("Nenhuma nota foi digitada.")