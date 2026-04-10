notas = [7, 8.5, 9, 6, 10]

print("Notas:")
for nota in notas:
    print(nota)

print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
print(f"Média: {sum(notas)/len(notas):.2f}")