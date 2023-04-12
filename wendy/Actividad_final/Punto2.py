W = 1

for i in range(1,10):
    result = W * 9 + (i + 1)
    print(f'{W} x 9 + {i+1} = {result}')
    W = result + W