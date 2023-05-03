T = 3
total_garrafas = 0

for i in range(T):
    n, k = map(int, input().split())
    if k > n:
        total_garrafas = n
    else:
        while n >= k:
            n = n // k
            total_garrafas += n
            n = (n % k) + n

    print(f'{total_garrafas}')
    
