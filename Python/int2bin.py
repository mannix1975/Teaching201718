''' Simple program to convert integers to binary and vice versa

Mark Foley October 2013
'''

print('Int to binary')

try:
    int_str = input('Give me an int: ')
    myInt = int(int_str)

    bin_str = ''
    while myInt > 0:
        bin_str = str(myInt % 2) + bin_str
        myInt //= 2

    print('The binary of', int_str, 'is', bin_str)

    print('\nBinary to int')
    bin_str = input('Give me a binary string: ')

    temp = bin_str
    new_int = 0
    power = 0
    while len(temp) > 0:
        bit = int(temp[-1])
        new_int = new_int + bit * 2 ** power
        temp = temp[:-1]
        power += 1

    print(bin_str, 'to integer is', new_int)

except ValueError as e:
    print("You made an error. Try again.")
