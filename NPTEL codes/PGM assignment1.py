def ifPrime(n):
    fac=[]
    for i in range(1,n+1):
        if n%i==0:
            fac.append(i)
        if fac==[1,n]:
            return True
        elif i==n:
            return False
        else:
            continue
def primeproduct(m):
    if m<=2:
        return False
    for i in range(2,m):
        if m%i==0:
            j=int(m/i)
            if ifPrime(i)==True and ifPrime(j)==True:
                return True
            else:
                continue
        elif i==m-1:
            return False
        else:
            continue
def delchar(s,c):
    dels=""
    for char in s:
        if len(c)!=1:
            return s
        elif char==c:
            continue
        else:
            dels=dels+char
    return dels
def shuffle(l1,l2):
    l3=[]
    if len(l1)>len(l2):
        n=len(l1)
    else:
        n=len(l2)
    for i in range(0,n):
        if l1[i:i+1]:
            l3.append(l1[i])
        if l2[i:i+1]:
            l3.append(l2[i])
    return l3
print(shuffle([0],[1,3,5]))