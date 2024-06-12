def soma(a,b):
    return a+b
def quadrado (a):
    return a**2
def hipotenusa (cateto1, cateto2):
    return soma(quadrado(cateto1), quadrado(cateto2))**(1/2)
def simples(cor):
    if cor == 'azul':
        return 'acertou'
def medio (cor):
    if cor =='azul':
        return 'arrasou'
    else:
        return'errouu, tenta de novo'
def completo (cor):
    if cor == 'azul':
        return 'arrasou'
    elif cor=='vermelho':
        return 'errou com força'
    else:
        return 'tente outra cor'
numeros = [1,2,3,4,5]
print(numeros[0])
print(numeros[-1])
numeros[0]
print(numeros)

contador=0
while contador < 10:
    print(contador)
    contador += 1
    
for i in range (10):
    print(i)
for item in [1,45, 'a',[3,5]]:
    print(item)
for letra in 'minha string':
    print(letra)



def desenhar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)
num_linhas = 4
desenhar_triangulo(num_linhas)
