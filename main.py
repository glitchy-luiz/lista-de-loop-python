#exc1
'''while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            break
        else:
            print("O numero deve ser entre 0 e 10")
    else:
        print("Você deve digitar um numero")'''

#exc2
'''nome = input("Diga o nome: ")
while True:
    nome = input("Diga seu nome: ")
    if len(nome) >= 3:
        break
    print("Opção invalida!")

while True:
    idade = input("Diga sua nota: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 0 and idade <= 10:
            break
        print("O numero deve ser entre 0 e 10")
    else:
        print("Você deve digitar um numero")

salario = input("diga seu salario: ")
while not salario.isnumeric():
    salario = input("Diga seu salario: ")

sx = input("Diga f ou m\n->")
while sx != 'f' and sx != 'm':
    sx = input("Diga f ou m\n->")

ec = input("Diga s,c,v,d:\n->")
while not (ec =='s' or ec =='c' or ec =='v' or ec =='d' or):
    print("Opção invalida!")
    ec = input("Diga s,c,v,d:\n->")'''

#exc3
'''a = 80000
b = 200000
anos = 0
while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)'''

#exc4
'''quant = 0
soma = 0
while quant < 5:
    num = input(f"digite o {quant+1} número: ")
    while not num.isnumeric():
        print("Diga um numero")
        num = input("digite um número: ")
    num = int(num)
    soma += num
    quant += 1
print(f"A soma dos numeros foi {soma} e a media foi {soma/quant}")'''

#exc5
'''a = 2
b = 8
if a > b:
    aux = a
    a = b
    b = aux
while a <= b:
    print(a)
    a+=1'''

#exc6
'''usuario = input('Diga seu nome de usuario: ')
senha = input("diga sua senha: ")
while usuario == senha:
    print("usuario n pode ser igual a senha")
    usuario = input('Diga seu nome de usuario: ')
    senha = input("diga sua senha: ")'''

#exc7
'''num = input("Digite um número: ")
tab = 1
while not num.isnumeric():
        print("Diga um numero entre 1 a 10")
        num = input("Digite um número: ")
num = int(num)
print(f'Tabuada do {num}:\n')
while tab <=10:
    mult = num * tab
    print(f'{num} X {tab} = {mult}')
    tab += 1'''

'''num = 1
multiplo = 1
while multiplo <= 10:
    tab = 1
    print(f'Tabuada do {num}:')
    while tab <= 10:
        print(f'{num} X {tab} = {num*tab}')
        tab += 1
    multiplo += 1
    num += 1
    print()'''

#exc8
'''a = 1
print(a)
b = 1
print(b)
i = 0
while i < 20:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1'''

#exc9
'''qtd = 0
pares = 0
while qtd < 10:
    num = input(f'Diga o {qtd+1} numero: ')
    while not num.isnumeric():
        num = input(f'Diga o {qtd+1} numero: ')
    num = int(num)
    if num % 2 == 0:
        pares += 1
    qtd += 1
print(f'Vc digitou {pares} pares e {qtd - pares} impares')'''

#exc10
'''num = 5
fatorial = num
fatorial_sting = f'{num}! = {num}'
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_sting += f'*{num}'
    print(fatorial_sting)
fatorial_sting += f' = {fatorial}'
print(fatorial_sting)'''

#exc11
'''num = 117991
i = 2
while i < num**0.5:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print('Não é primo')
        break
    i+=1
if i >= num**0.5:
    print('é primo')'''

#exc13
'''salario = 1000
taxa = 0.015
partida = 1995
while partida < 2024:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)'''

#exc14
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    num = input("diga um numero entre 0 e 100, e maior que 100 para sair\n -> ")
    while not num.isnumeric():
        num = input("diga um numero entre 0 e 100, e maior que 100 para sair\n -> ")
    num = int(num)
    if num<= 25:
        primeiro += 1
    elif num <=50:
        segundo+=1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto += 1
    else:
        break
