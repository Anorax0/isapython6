'''

zdanie = '   ala ma kota    '

zdanie = zdanie.strip()
zdanie = zdanie.capitalize()
# zdanie = zdanie + '.'
zdanie += '.'

print((zdanie))


zdanie = input('Podaj jakieś zdanie:')

zdanie = zdanie.strip()
zdanie = zdanie.capitalize()
# zdanie = zdanie + '.'
zdanie += '.'
print(zdanie)


a = int(input('Podaj pierwszą liczbę: '))
b = input('Podaj drugą liczbę: ')
b = int(b)
suma = a+b
# print('Suma ' + str(a) + ' i ' +  str(b) + '  jest równa ' + str(suma))
print(f'Suma liczby {a} i {b} jest równa {suma}.')

'''
zdanie1 = 'Ala ma kota. ' #\n
zdanie2 = 'Ania ma psa.'
# print(zdanie1 + zdanie2)
print(zdanie1, end='') #print nie wkleja znaku przejście do nowej linii \n
print(zdanie2)