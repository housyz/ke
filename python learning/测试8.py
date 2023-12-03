n,m = map(input().split())
k = input()
for i in range(k):
    a,b=map(input().split())
for i in range(2*n+1):
    if i % 2 == 0:
        for g in range(4*n+1):
            if g % 4 == 0:
                print("+",end="")
            else:
                print("-",end="")
            if g == 4*n:
                print()
    if i % 2 == 1:
        for g in range(4*n+1):
            if g % 4 == 0:
                print("|",end="")
            else:
                print(" ",end="")
            if g == 4*n:
                print()
