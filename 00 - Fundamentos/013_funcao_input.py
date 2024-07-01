# Função print

# nome = input("Qual seu nome? ")
# print(f'O seu nome é {nome}')

numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")

# Neste caso houve uma concatenação de string
print(f"A soma dos números é: {numero_1 + numero_2}  - concatenação")

numero_3 = input("Digite o primeiro número: ")
numero_4 = input("Digite o segundo número: ")

int_numero_3 = int(numero_3)
int_numero_4 = int(numero_4)

# Neste caso houve um casting
print(f"A soma dos números é: {int_numero_3 + int_numero_4} ")
