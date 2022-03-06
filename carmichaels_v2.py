def gcd(a,b):
    while (a>0):
        b=b%a
        (a,b)=(b,a)
    return b    

def carmichael(n):
    n=int(n)
    k=2
    a=1
    alist=[]

    while not ((gcd(a,n))==1):
        a=a+1

    while ((gcd(a,n))==1) & (a<=n) :
        alist.append(a)
        a=a+1
        while not ((gcd(a,n))==1):
            a=a+1

    timer=len(alist)
    while timer>=0:
        for a in alist:
            if (a**k)%n==1:
                timer=timer-1
                if timer <0:
                    break
                pass
            else:
                timer=len(alist)
                k=k+1
    return k

p = carmichael(20000)
print(p)
