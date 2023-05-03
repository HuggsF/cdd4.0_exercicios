number_one = int(input('number one?'))
number_two = int(input('number two?'))

while number_one == number_two:
    number_two = int(input('number two can not be same as number one.\nnumber two? '))

if number_one>number_two:
    print(f'{number_one} is bigger than {number_two}')
else:
    print(f'{number_two} is bigger than {number_one}')
