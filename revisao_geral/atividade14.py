apple_price = 1.30
apple_quantity = int(input('How many apples do you want?'))
if apple_quantity >= 12:
    apple_price = 1

print(f'You brougth {apple_quantity} apples and spent {apple_quantity*apple_price} dollars.')