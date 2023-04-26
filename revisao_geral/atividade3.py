##Seccond Question
positives = []
negatives = []
keepo_going = "Y"
while keepo_going == "Y":
    result = int(input(f'number != 0: '))
    if result == 0:
        while result == 0:
            result = int(input(f'!= 0: '))
    if result < 0:
        print(f'{result} is a Negative Number')
        negatives.append(result)
    else:
        print(f'{result} is a Positive Number')
        positives.append(result)

    keepo_going = input(f'More numbers? Y/N').title()

print(f'''
===================================
Here is your positives number list! 
{positives}
Here is your positives number list!
{negatives}
===========Cya!====================''')
