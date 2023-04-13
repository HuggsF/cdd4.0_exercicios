count = 0
count2 = 0
for x in range(10):
    num = int(input("digita 1 numero: "))
    if num >= 10 and num <= 20:
       count+=1
    else:
        count2+=1
print(count, count2)