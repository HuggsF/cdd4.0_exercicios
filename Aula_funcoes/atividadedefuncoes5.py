def yoloswagscope(float):
    if float > 0:
        return "P"
    elif float < 0:
        return "N"
    elif float == 0:
        return "Z"

print(yoloswagscope(10))
print(yoloswagscope(0))
print(yoloswagscope(-10))