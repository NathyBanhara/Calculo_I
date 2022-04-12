import math

def get_cuberoot(x): #faz a raiz cúbica
    if x < 0:
        x = abs(x)
        cube_root = pow(x,1/3)*(-1)
    else:
        cube_root = pow(x,1/3)

    return cube_root

def raio(x, y, v):
    r = get_cuberoot((y*v)/(math.pi*2*x))
    return r

def altura(v, r):
    return v/(math.pi*r**2)

v = float(input("Volume: "))
v /= 1000000 #converte de cm3 para m3

x = float(input("Custo do material do topo e da base: "))
y = float(input("Custo do material dos lados: "))


r = raio(x, y, v)
h = altura(v, r)

areaTotal = (2*math.pi*(r**2)) + (2*math.pi*h*r)
custoTotal = (x*(2*math.pi*(r**2))) + (y*(2*math.pi*h*r))
