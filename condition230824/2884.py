h, m = map(int, input().split())

if m >= 45:
    H = h
    M = m-45
elif m < 45:
    if h != 0:
        H = h-1
        M = 60+m - 45
    elif h == 0:
        H = 23
        M = 60+m - 45

print(H, M)
