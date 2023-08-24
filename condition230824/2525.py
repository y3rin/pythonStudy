# 몇분뒤 계산기
h, m = map(int, input().split())
time = int(input())

timeh = time//60
timem = time % 60

if m+timem < 60:
    if h+timeh > 23:
        H = h+timeh - 24
        M = m+timem
    elif h+timeh <= 23:
        H = h+timeh
        M = m+timem
elif m+timem >= 60:
    if h+timeh+1 > 23:
        H = h+timeh+1 - 24
        M = m+timem-60
    elif h+timeh+1 <= 23:
        H = h+timeh+1
        M = m+timem-60

print(H, M)
