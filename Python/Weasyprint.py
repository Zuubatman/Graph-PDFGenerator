from weasyprint import HTML
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def criaPdf(): 
    date = datetime.now()

    print(date)

    f = open("opa.html", "r")

    html_str = f.read()

    print(html_str)
    new_html = html_str.replace("**Date**", str(date))
    new_html = new_html.replace("**Bar**", "bars.png") 
    new_html = new_html.replace("**Functions**", "funcoes.png") 

    print(new_html)

    with open('opa2.html', 'wt') as new_file:
        new_file.write(new_html)
        new_file.close()
    
    # htmldoc.write_pdf('opa2.pdf')

    htmldoc = HTML('opa2.html')
    htmldoc.write_pdf('opa2.pdf')

    #CSS(string='@page { size: A3; margin: 1cm }')                                                  



def opa():

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

    criaPdf()
    

criaPdf()