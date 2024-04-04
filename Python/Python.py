
import random
import numpy as np


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np




class Bilhete :
    def __init__(self, epar, pares, impares):
        self.epar = epar
        self.pares = pares
        self.impares = impares

    def teste(self):
        print('lololololool')
    

class Aposta : 
    def __init__(self, id, numeros):
        self.id = id
        self.numeros = numeros

    def mortalDeCostas(self):
        opaa = {"asd" : 4 , 'dsa': 'tirulitiruli'}
        print(opaa.keys())


def main () :
    
    # numeros = input('Digite uma lista de números: ')
    # lista = numeros.split(' ')
    # print(lista)

    # # multiplicador(lista)

    # # print('Dobro:', lista)

    # res = calculaPares(lista)

    # epar = res[0]
    # impares = res[1]
    # pares = res[2]

    # print('São todos pares? ' , epar)
    # print('Números ímpares encontrados: ', impares)

    # coisa = bilhete(epar=epar, pares=pares, impares=impares)

    # print(coisa.pares)

    # aposta = input("Digite 5 números separados por espaço: ")

    # # aposta_arr = aposta.split(' ') 

    # numeros_sorteados = sorteador()

    # print('abacate')
    # apostas = [[1,2,3,4,5], [6,7,8,9,10]]

    # print(estaContido([1,12,3,12,5], [1,2,3,4,5,6,8,9,10,11,12]), 1)
    # a = {'opa': [12,13,14,56], 'teste': 56}
    # print(a.items())

    # print((len(a.items())))
    # print(a.get('opa'))
    # print(a.keys())
    # print(a.values())
    # print(a.items())

    # a['abacate'] = 123456

    # c = Bilhete(True, [2,4,6,] , [1,3,5,])
    # h = Aposta(1001, [1,2,3,4,5])
    # print(c.pares)

    # print(a)
    # c.teste()
    # h.mortalDeCostas()

    a = np.arange(15).reshape(3,5)
    b = np.arange(30).reshape(6,5)
    c = np.array([[1,5,2,3], [4,5,6,0]])
    d = np.zeros((3,4))
    e = np.ones((10,10))
    f = np.empty((5,5))
    g = np.arange(10,20,2)
    h = np.arange(2, 5 , 0.2)
    i = np.arange(24).reshape(2,3,4)

    # print(c)
    # print(a.shape)
    # print(b.ndim)
    # print(a.dtype.name)
    # print(c.dtype)
    # print(d)
    # print(e)
    # print(f)
    # print(g)
    # print(h)
    # print(i)

    # asd = np.arange(4)
    # dsa = np.array([10,20,30,40])
    # coiso = dsa - asd 
    # print(coiso)
    # print(asd*dsa) #elemento
    # print(np.sin(asd))
    # print(asd > 0 )
    # print(asd @ dsa) #matriz

    x =  np.arange(300)
    y = np.sin(x) / x

    # fig = plt.figure()
    plt.plot(x, y) 
    plt.title('Título show de bola')
    plt.grid()
    plt.legend('Sin(x)/x')
    plt.savefig('Sin.png', dpi=300)

    te = np.arange(0 ,2, 0.1)

    plt.figure(figsize=(9, 3))
    plt.plot(te, te, label='linear')  # Plot some data on the (implicit) axes.
    plt.plot(te, te**2, label='quadratica')  # etc.
    plt.plot(te, te**3, label='cubica')
    plt.plot(te, te**4, label= 'biquadrada', linestyle='--')
    plt.title("Gráfico Legal")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.savefig('funcoes.png', dpi=300)


    plt.figure()
    plt.scatter(np.arange(10), np.arange(10) * np.cos(np.arange(10)))
    plt.scatter(np.arange(10), np.arange(10) * np.random.rand(10))
    plt.grid()
    plt.title('O loko')
    plt.savefig('scatter.png', dpi=300)

    plt.figure()
    plt.bar(np.arange(10), np.random.rand(10) * 10)
    plt.title("ASD")
    plt.grid()
    plt.savefig('bars.png', dpi=300)

    ol = np.arange(100)
    plt.figure()
    # plt.plot(ol,ol **2, label ='quadrática')
    plt.bar(ol, np.random.rand(len(ol)), label = 'barras')
    plt.scatter(ol, np.random.rand(len(ol)), label = 'pontos')
    plt.plot(ol, np.sin(ol) / ol, label='Sen(x)/x', color='red', linestyle='--')
    plt.title('Loucurada')
    plt.legend()
    plt.savefig('loucurada.png', dpi=300)


    plt.show()


def estaContido(aposta_arr, numeros_sorteados, tentativas): 
    acertos = 0
    for i in range (len(numeros_sorteados)) :
        for j in range (len(aposta_arr)) : 
            if numeros_sorteados[i] == aposta_arr[j]:
                acertos += 1
            if(acertos == 5):
                return True
    
    if tentativas <= 25:
        new = numeros_sorteados.append(random.randint(1, 50))
        estaContido(aposta_arr , new, tentativas + 1)
    

def jogar ():
    print('oi')


def sorteador():
    numeros_sorteados = []

    for i in range (5) :
        random_int = random.randint(1, 50)
        numeros_sorteados.append(random_int)
    
    return print(numeros_sorteados)

def multiplicador(lista):
    for i in range (len(lista)):
        lista[i] = int(lista[i]) * 2

    return lista

def calculaPares(lista) -> tuple:
    epar = True
    numerosimpares = []
    numerospares = []

    for i in range (len(lista)):
        numero = int(lista[i])

        if numero % 2 != 0 :
            epar = False
            numerosimpares.append(numero)
        else:
            numerospares.append(numero)
            

    return [epar , numerosimpares, numerospares]


main()