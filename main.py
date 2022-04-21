alpha = float(input())
w1 = float(input())
w2 = float(input())
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
counter = 0
b = 0
for i in range(100):
    if i%4 == 0:
        counter = 0
    x, y = inputs[i%4]
    f = 1 if (w1 * x + w2 * y) + b > 0 else 0
    E = int(x or y) - f
    print(f'{i} : {x}, {y} ,{w1}, {w2}, {f}, {E}, {counter}')
    if E != 0:
        w1 = w1 + alpha*x*E        
        w2 = w2 + alpha*y*E
        counter = 0
        b = b + alpha * E
    else:
        counter += 1
    if counter == 4:
        break
    

