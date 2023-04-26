age_in_years = int(input(f'How much years do you have?'))
age_in_moths = int(input(f'How much moths do you have in your age?'))
age_in_days = int(input(f'How much days do you have in your age?'))

age_in_days += (age_in_years*365)
age_in_days += (age_in_moths*30)


print(f'Your age in days is {age_in_days} days.')