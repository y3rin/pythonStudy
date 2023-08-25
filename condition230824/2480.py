a, b, c = map(int, input().split())

if a == b and b == c: #a==b==c
    win = 10000+a*1000
elif a == b or c == a:
    win = 1000 + a*100
elif b == c:
    win = 1000+b*100
else:
    maximum = ((a) if a > c else (c)) if a > b else (b) if b > c else (c) #max(a,b,c)
    win = maximum*100

print(win)
