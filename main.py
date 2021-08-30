#Lista de exercicios 01 - Estruturas em sequência Endereço: https://wiki.python.org.br/EstruturaSequencial
q = int(input('Informe a questão: '))
if q == 1:
    #Botei a pergunta e a resolução em cada 'switch'
    print(q, 'Faça um Programa que mostre a mensagem "Alo mundo" na tela.')
    print('Alo mujndo')
if q == 2:
   print(q, 'Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].')
   numero = int(input("Digite um número: "))
   print("O número digitado foi ", numero)
if q == 3:
    print(q, 'Faça um Programa que peça dois números e imprima a soma.')
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    print('A soma de', a, '+', b, ' = ', a + b)
if q == 4:
    print(q, 'Faça um Programa que peça as 4 notas bimestrais e mostre a média.')
    nota1 = float(input('Informe a primeira nota:'))
    nota2 = float(input('Informe a segunda nota:'))
    nota3 = float(input('Informe a terceira nota:'))
    nota4 = float(input('Informe a quarta nota:'))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print('A media foi de ', media)
if q == 5:
    print(q, 'Faça um Programa que converta metros para centímetros.')
    m = float(input('Digite a quantidade de metros: '))
    cm = m * 100

    print(m, "m é igual a ", cm, 'cm')
if q == 6:
    print(q, 'Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.')
    raio = float(input('Digite o raio do circulo: '))
    area = 3.14 * raio

    print('A área do circlo é de: ', area)
if q == 7:
    print(q, 'Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.')
    lados = float(input('Digite o tamanho dos lados do quadrado: '))
    area = lados**2
    dobro = area * 2

    print('A área do quadrado é ', area, ' e o dobro dela é ', dobro)
if q == 8:
    print(q, 'Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês')
    qtd_hora = float(input('Quanto você ganha por hora?'))
    horas_mes = int(input('Quantas horas você trabalha no mês?'))

    salario = qtd_hora * horas_mes
    print('O seu salário no final do mês será de R$', salario)
if q == 9:
    print(q, 'Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).')
    F = float(input('Quantidade de °F: '))
    C = (F - 32) / 9

    print(F, ' °F são iguais a ', C, ' °C')
if q == 10:
    print(q, 'Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.')
    C = float(input('Quantidade de °C: '))
    F = (C * 1.8) + 32

    print(C, ' °C são iguais a ', F, ' °F')
if q == 11:
    print(q, '''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.''')
    x = int(input('Digite um número inteiro: '))
    y = int(input('Digite outro número inteiro: '))
    real = float(input('Digite um número real'))

    a = (x * 2) + (y / 2)
    b = (x * 3) + real
    c = real ** 3

    print("a : ", a, "\nb : ", b, "\nc : ", c)
if q == 12:
    print(q, 'Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58')
    altura = float(input('Digite a altura: '))
    peso_ideal = (72.7 * altura) - 58

    print('Peso ideal: ', peso_ideal)
if q == 13:
    print(q, '''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7''')
    sexo = input('Digite (F)-Feminino, (M)-Masculino: ').upper()
    if sexo == 'M':
        altura = float(input("Digite a altura: "))
        homem = (72.7 * altura) - 58
        print('Homem: %2.f' % homem)
    elif sexo == 'F':
        altura = float(input("Digite a altura: "))
        mulher = (62.1 * altura) - 44.7
        print('Mulher: %2.f' % mulher)
    else:
        print('Sexo Inválido')
if q == 14:
    print(q, 'João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.')
    peso = int(input("Digite o peso dos peixes: "))
    execesso = peso - 50
    multa = execesso * 4

    if execesso < 1:
        print("João não terá que pagar multa")
    else:
        print("A multa que joão terá que pagar será de: ", multa)
if q == 15:
    print(q, '')