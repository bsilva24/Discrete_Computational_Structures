from time import sleep

#Exercicio 1

def implica(a, b):
    return not a or b
#Fim do Exercicio 1


#Exercicio 2
while True:
    p = str(input("Insira um valor lógico para p [V/F]: ")).strip().upper()
    if p == "V":
       p = True
       break
    elif p == "F":
       p = False
       break
    else:
       print("Argumento introduzido inválido!")
       
       
while True:   
    q = str(input("Insira um valor lógico para q [V/F]: ")).strip().upper()
    if q == "V":
       q = True
       break
    elif   q == "F":
       q = False
       break
    else:
       print("Argumento introduzido inválido!")
       
       
while True:
    r = str(input("Insira um valor lógico para r [V/F]: ")).strip().upper()
    if r == "V":
       r = True
       break
    elif   r == "F":
       r = False
       break
    else:
       print("Argumento introduzido inválido!")
       
while True:
    s = str(input("Insira um valor lógico para s [V/F]: ")).strip().upper()
    if s == "V":
       s = True
       break
    elif   s == "F":
       s = False
       break
    else:
       print("Argumento introduzido inválido!")
while True:
    t = str(input("Insira um valor lógico para t [V/F]: ")).strip().upper()
    if t == "V":
       t = True
       break
    elif   t == "F":
       t = False
       break
    else:
       print("Argumento introduzido inválido!")   
while True:
    u = str(input("Insira um valor lógico para u [V/F]: ")).strip().upper()
    if u == "V":
       u = True
       break
    elif   u == "F":
       u = False
       break
    else:
       print("Argumento introduzido inválido!")
        
def a():
    exp1_9a = implica(p,q) and implica(p,r)
    exp2_9a = implica(p, (q and r))
    sleep(1)
    print("As expressões do exercicio 9 a) são (p → q) ∧ (p → r) e p → (q ∧ r)")
    sleep(1)
    equival(exp1_9a, exp2_9a)
    
    
def c():
    exp1_9c = implica(p, r) or implica(q, r)
    exp2_9c = implica((p and q), r)
    sleep(1)
    print("As expressões do exercicio 9 c) são (p → r) V (q → r) e (p ∧ q) → r")
    sleep(1)
    equival(exp1_9c, exp2_9c)

def e():
    exp1_9e = implica((p or q), p)
    exp2_9e = implica(q, p)
    sleep(1)
    print("As expressões do exercicio 9 e) são p V q → r e q → p")
    sleep(1)
    equival(exp1_9e, exp2_9e)
    
def g():
    exp1_9g = implica(p, q)
    exp2_9g = implica((p and not q), False)
    sleep(1)
    print("As expressões do exercicio 9 g) são p → q e (p ∧ ¬ q) → False")
    sleep(1)
    equival(exp1_9g, exp2_9g)
    
def i():
    exp1_9i = implica(s, t) and (u or t or not s)
    exp2_9i = implica(s, t)
    sleep(1)
    print("As expressões do exercicio 9 i) são (s → t) ∧ (u V t V ¬ s) e s → t")
    sleep(1)
    equival(exp1_9i, exp2_9i)
    
def equival(a,b):
    if a == b:
        print("As expressões são equivalentes!")
    else:
        print("Não são equivalentes!")

a()
c()
e()
g()
i()
#Fim Exercicio 2

#Exercicio 3
a = int(input('Introduza um número inteiro: ')) 
b = int(input('Introduza um valor para o módulo: '))
mod = 0

def mod(a, b):
        mod = a % b
        return mod

print(f'O resultado de {a} mod {b} = {mod(a, b)}')
#Fim do Exercicio 3

#Exercicio 4
a = int(input('Introduza um valor numérico (dividendo): '))
b = int(input('Introduza outro valor numérico (divisor): '))

def mdc(a, b):
    while b != 0:
        resto = b
        b = a % b
        a = resto
    return a

print(f'O MDC entre o numero {a} e o numero {b} é {mdc(a, b)}')
#Fim do Exercicio 4

#Exercicio 5
a = int(input('Introduza um valor numérico (dividendo): '))
b = int(input('Introduza outro valor numérico (divisor): '))

def mdc_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mdc_recursivo(b, a % b)
print(f'O MDC entre o numero {a} e o numero {b} é {mdc_recursivo(b, a % b)}')
#Fim do Exercicio 5


    
    
    
    