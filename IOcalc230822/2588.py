a = int(input())
b = int(input())

listb = list(map(int, str(b)))
print(a*listb[2])
print(a*listb[1])
print(a*listb[0])
print(a*b)
