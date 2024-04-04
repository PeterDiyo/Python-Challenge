#Brute force
def gcd(m,n):
    fm = []
    for i in range(1, m+1):
        if(m % i) == 0:
            fm.append(i)
    fn = []
    for j in range(1, n+1):
        if(n % j) == 0:
            fn.append(j)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return (cf[-1])


#Better approach
def gcd(m, n):
    cf = []
    for i in range (1, min(m,n)+1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    return(cf[-1])    


 #Without list[]
def gcd(m,n):
    for i in range(1, min(m,n)+1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return (mrcf)      

#Scan backwards
def gcd(m,n):
    i = min(m,n)
    while i > 0:
        if (m % i) == 0 and (n % i) == 0:
            return (i)
        else:
            i = i-1


#Euclid's algorithm (i)
def gcd(m,n):
    #assume m>=n
    if m < n:
        (m, n) = (n, m)
    if (m % n) == 0:
        return (n)      
    else:
        diff = m - n
        #diff > n? possible!
        return (gcd(max(n, diff), min(n, diff)))
    
#Euclid's algorithm (2)
def gcd(m,n):
    if m < n:  #Assume m>=n
        (m,n) = (n,m)
    while (m%n) != 0:
        diff = m-n
        #diff>n? Possible!
        (m,n) = (max(n,diff), min(n,diff))     
    return (n)           