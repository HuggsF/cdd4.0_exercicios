##First Question
keep_going = str("Y")
averages = []

while keep_going == "Y":
    first_number = float(input(f'first grade? '))
    seccond_number = float(input(f'seccond grade? '))
    average = (first_number + seccond_number)/ 2

    print(f'{average}')
    averages.append(average)

    if average >= 7:
        print(f'Approved')
    elif average >=4:
        print(f'Recovery')
    else:
        print(f'Disapproved')

    keep_going = input("Keep Going? Y/N.").title()

print(f'''
==========================
Here is your average list! 
{averages}
===========Cya!===========''')