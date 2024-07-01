a = "A"
b = "B"
c = 1.1

formato = "a={} b={} c={:.2f}".format(a, b, c)
print(formato)

# Pegando os indices
formato = "a={0} b={1} c={2:.2f}".format(a, b, c)
print(formato)

# Parametro nomeado
formato = "a={a} b={b} c={c:.2f}".format(a=a, b=b, c=c)
print(formato)
