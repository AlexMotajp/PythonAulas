# Vamos testar um fibonacci com funções

def fibTest(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibTest(2000)