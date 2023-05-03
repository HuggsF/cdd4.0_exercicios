inicial_hour = int(input('Inicial hour of your chess round?'))
final_hour = int(input('Your final hour?'))

if inicial_hour < final_hour:
    print(f'your game take {final_hour - inicial_hour} hour')
else:
    print(f'your game take {(24 - inicial_hour)+final_hour} hour')
