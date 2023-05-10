def piramide_numerica(x):
    for x in range(0,x+1):
        for y in range(x+1):
            print(y+1, end="")
        print("")
piramide_numerica(9)