print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_a(a,b):
    r=a-b
    return r
def multi_b(a,b):
    m=a*b
    return m
def div_c(a,b):
    d=a/b
    return d
# Llamadas a funciones
print("Calculando sumas")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")

print("Calculando resta")
a1=int(input("Ingresa el primer numero "))
a2=int(input("Ingresa el segundo numero "))
resta=resta_a(a1,a2)
print(f"la resta de {a1} - {a2} es {resta}")

print("Calculando multiplicacion")
b1=int(input("Ingresa el primer numero "))
b2=int(input("Ingresa el segundo numero "))
mult=multi_b(b1,b2)
print(f"la multiplicacion de {b1} * {b2} es {mult}")

print("Calculando division")
c1=int(input("Ingresa el primer numero "))
c2=int(input("Ingresa el segundo numero "))
divi=div_c(c1,c2)
print(f"la division de {c1} / {c2} es {divi}")