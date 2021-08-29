def cmmdc(n,m):
    if m == 0:
        return n
    return cmmdc(m,n % m)



n=int(input())
m=int(input())
print(cmmdc(n,m))