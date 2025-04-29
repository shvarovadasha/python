for i in range(1, int(input()) + 1):
    print(int("".join([str(x) for x in range(1, i + 1)] + [str(x) for x in range(i - 1, 0, -1)])))
