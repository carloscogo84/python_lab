"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador < 20:
    contador += 1

    if contador == 6:
        print("Não mostrado o número 6")
        continue

    if contador >= 10 and contador <= 13:
        continue

    print(contador)

    if contador == 15:
        break

print("Acabou o loop")
