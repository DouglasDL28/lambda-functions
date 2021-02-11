# Universidad del Valle de Guatemala
# Análisis y Diseño de Algoritmos
# Douglas de León Molina
# Carné 18037 

f = lambda x: x + 1

g = lambda x: 2 * x

h = lambda x, y: x**2 + y**2

cero = lambda f, x: x

uno = lambda f, x: f(x)

dos = lambda f, x: f(f(x))

tres = lambda f, x: f(f(f(x)))

sucesor = lambda n: lambda f, x: f(n(f(x)))

suma = lambda a: lambda b: lambda f, x: a(f(b(f(x))))

mult = lambda a: lambda b: lambda f, x: a(b(f(x)))

