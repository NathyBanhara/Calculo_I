def equacao(x):
    e = 2.718281828459045235360287
    return e**(-x) - 2*(x**2) + 4

def sinais(x):
    if x >= 0:
        return True
    return False

def maior(x, y):
    if x > y:
        return x
    return y

while True:
    x, y = map(float, input().split())
    f_x = equacao(x)
    f_y = equacao(y)
    sinal_x = sinais(f_x)
    sinal_y = sinais(f_y)
    if sinal_x == sinal_y:
        print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
    else:
        while abs(x-y) > 0.1:
            novo = (x+y)/2
            f_novo = equacao(novo)
            sinal_novo = sinais(f_novo)
            if sinal_novo == sinal_x:
                f_x = f_novo           
                x = novo
            else:
                f_y = f_novo
                y = novo
        aux = maior(x, y)
        if aux == x:
            novo = y
            y = x
            x = novo
        print(f"[{x}, {y}]")
        break

                
    


