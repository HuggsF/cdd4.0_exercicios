##Fifith Question

keep_going = "y"
ages = []
while keep_going == "y":
    age = int(input(f'Input your age.'))
    print(f'Your birth year is {2023 - age}')
    ages.append(age)
    keep_going = input('Another one?')

print(f'{ages}')