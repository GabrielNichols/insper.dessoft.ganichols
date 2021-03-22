#sistema contador de porcentagens de idades dentro de um hospital


# validar condicionais
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
faixa6 = 0
continuar = True

# while para escrever o imput de todas as idades até escrever um numero negativo para parar
while continuar:
    idade = int(input ('Idade '))
    if idade < 0:
        continuar = False  #"return de while"
    elif idade < 12:   # 0 até 11
        faixa1 += 1
    elif idade < 18:   # 12 até 17
        faixa2 += 1    
    elif idade < 26:   # 18 até 25
        faixa3 += 1
    elif idade < 36:   # 26 até 35
        faixa4 += 1
    elif idade < 60:   # 36 até 59
        faixa5 += 1
    else:              # >= 60
        faixa6 += 1

#condicional para colocar a porcentagem
t = (faixa1 + faixa2 + faixa3 + faixa4 + faixa5 + faixa6)/100

#imprimir relações em porcentagem
print ('entre 0 e 11: {:.2f}%'.format(faixa1/t))
print ('entre 12 e 17: {:.2f}%'.format(faixa2/t))
print ('entre 18 e 25: {:.2f}%'.format(faixa3/t))
print ('entre 26 e 35: {:.2f}%'.format(faixa4/t))
print ('entre 36 e 59: {:.2f}%'.format(faixa5/t))
print ('acima de 60: {:.2f}%'.format(faixa6/t))

print('Eric')