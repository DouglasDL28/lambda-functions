# Universidad del Valle de Guatemala
# Análisis y Diseño de Algoritmos
# Douglas de León Molina
# Carné 18037 

print("""
----------------
PROYECTO #1
FUNCIONES LAMBDA
----------------
""")

f = lambda x: x + 1
print("a) f(3) =", f(3), "\n")

g = lambda x: 2 * x
print("b) g(5) =", g(5), "\n")

h = lambda x, y: x**2 + y**2
print("c) h(4, 3) =", h(4, 3), "\n")

cero = lambda f: lambda x: x
print("d) cero(f, 0) =", cero(f)(0), "\n")

uno = lambda f: lambda x: f(x)
print("e) uno(f, 0) =", uno(f)(0), "\n")

dos = lambda f: lambda x: f(f(x))
print("f) dos(f, 0) =", dos(f)(0), "\n")

tres = lambda f: lambda x: f(f(f(x)))
print("g) tres(f, 0) =", tres(f)(0), "\n")

sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
print("h) sucesor(tres, f, 0) =", sucesor(tres)(f)(0), "\n")

suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
print("i) suma(tres, dos, f, 0)", suma(tres)(dos)(f)(0), "\n")

mult = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
print("j) mult(tres, dos, f, 0) =", mult(tres)(dos)(f)(0), "\n")
