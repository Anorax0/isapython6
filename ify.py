zdanie = input('Podaj zdanie: ')

if 'a' in zdanie:
    print(("Jest mała litera a"))
elif 'A' in zdanie:
    print('Jest duża litera A')
    if zdanie.count('A') > 2:
        print("Cos duży tych literek A")
elif 'x' in zdanie:
    print('Litera x w zdaniu.')
else:
    print("Nic nie znalazłem.")