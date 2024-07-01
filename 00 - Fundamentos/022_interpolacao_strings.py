"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Luiz"
preco = 10000.95897643
variavel = "Luiz, o preço total foi de R$ 1000.95"
print(variavel)

# Interpolação

variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))
