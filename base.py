alpha = float(input())
w1 = float(input())
w2 = float(input())
gate = input()
AND = lambda x, y: int(x and y)
NAND = lambda x, y: int(not (x and y))
OR = lambda x, y: int(x or y)
NOR = lambda x, y: int(not (x or y))
XOR = lambda x, y: int(x ^ y)
XNOR = lambda x, y: int(not (x ^ y))
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
counter = 0
b = 0


def Gate_(w1, w2, b, gate):
    for i in range(100):
        if i % 4 == 0:
            counter = 0
        x, y = inputs[i % 4]
        f = 1 if (w1 * x + w2 * y) + b > 0 else 0
        E = AND(x, y) - f
        print(f'{i} : {x}, {y} ,{w1}, {w2}, {f}, {E}, {counter}')
        if E != 0:
            w1 = w1 + alpha * x * E
            w2 = w2 + alpha * y * E
            counter = 0
            b = b + alpha * E
        else:
            counter += 1
        if counter == 4:
            break
