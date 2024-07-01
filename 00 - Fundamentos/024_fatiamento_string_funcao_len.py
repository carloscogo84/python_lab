"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[5])
print(variavel[-4])

# Fatiamento
print(variavel[4:])  # indice 4 até o fim (:)
print(variavel[4:7])
print(variavel[:5])
print(variavel[-8: -2])
print(len(variavel))
print(len(variavel[3]))
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[::])
print(variavel[::-1])
