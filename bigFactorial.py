n = int(input())

# For large N >= 25, factorial ends with at least four zeros
if n >= 25:
    print(0)
else:
    fact = 1
    for i in range(1, n + 1):
        fact = (fact * i) % 10000
    print(fact)