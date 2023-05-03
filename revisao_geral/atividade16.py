count = 30
a = []
number = 1
while count > 0:
    if number%2!=0:
        a.append(number)
        count-=1
    number+=1
print(f'{a}')