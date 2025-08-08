# Q1.A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

# Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

# Q2.Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

# Q3.Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

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