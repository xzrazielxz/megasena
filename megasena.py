from random import randint
from time import sleep
mjog = list()
lista = list()
listas = list()
cont = result = 0
print('—' * 35)
print('«MEGA $ENA LANCES»'.center(35))
print('—' * 35)
apos = int(input('|———————» Aposta [6/15] >>>>>>>> '))
while True:
    if apos < 6 or apos > 15:
        print('<<< Opção invalida >>>'.center(35))
        apos = int(input('|———————» Tente novamente >>>>>> '))
    else:
        break
sleep(1)
print('·' * 35)
print('Dados recebidos!!!'.center(35))
print('·' * 35)
sleep(1)
print('|————————» Hora de Jogar «—————————')
sleep(1)
while len(mjog) < apos:
    num = int(input('|——————» Digite um numero: >>>>> '))
    if num not in mjog and num != 0:
        if num > 0 and num <= 60:
            mjog.append(num)
    if num == 0:
        if len(mjog) >= 6:
            break
print('=-=' * 13)
print('PROCE$$ANDO...'.center(35))
print('=-=' * 13) 
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
    if len(lista) == 6:
        result += 1
        for x in lista:
            if x in mjog: cont += 1
        if cont == 6:
            break
        cont = 0
        for s, numero in enumerate(lista):
            print(f'| {numero} '.ljust(5), end = ' ')
            if s == 5:
                print()
                print('—' * 35)
        lista.clear()
vpos = [3.50, 24.50, 98.00, 294.00, 735.00,
        1617.00, 3234.00, 6006.00,
        10510.50, 17517.00]
invest = result * vpos[apos-6]
print('Tá quase lá...')
sleep(2)
print('—' * 35)
print('Resultados'.center(35))
print('—' * 35)
print(f'Total de jogos: {result}')
print(f'Investimento: R$ {invest:.2f}')
cano = cmes = cdia =  0
tempo = result / 2
while tempo > 0:
    tempo = tempo - 52
    cano += 1
    if result <= 52:
        tempo -= 4
        cmes += 1
print(f'Tempo: Aprox. {cano} anos.')
if cmes > 0:
    print(f'e {cmes} meses ')
print('—' * 35)

