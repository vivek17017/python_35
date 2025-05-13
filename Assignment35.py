"""
#Q1
def lcm(a,b):
    x=2
    jcb=1
    while a*b>1:
        if a%x==0 or b%x==0:
            if a%x==0:
                a=a/x
            if b%x==0:
                b=b/x
            jcb=jcb*x
        else:
            x=x+1
    return jcb
print(lcm(14,16))



#Q2
def count(s1):
    a=0
    i=0
    while i<len(s1):
        if s1[i]==' ':
            i+=1
            continue
        else:
            while s1[i]!=' ':
                i+=1
            else:
                a+=1
    return a
x=count(" my d name is  vivek  ")
print(x)

#Q3

def create(a,b):
    l1=[]
    for e in range(a+1,b):
        i=2
        while i<e:
            if e%i==0:
                break
            i+=1
        else:
            l1.append(e)
    return l1
x=create(5,100)
print(x)


#Q1
def lcm(a,b):
    L=a if a>b else b
    while a*b>=L:
        if L%a==0 and L%b==0:
            return L
        L+=1

print(lcm(14,16))

#Q2
def countWords(text):
    return len(text.split(' '))
print(countWords(" my d name is  vivek  "))



#Q3
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def listofPrime(a,b):
    return [x for x in range(a+1,b) if isprime(x)]
print(listofPrime(1,10))

#Q4
def filter(s1):
    l1=[]
    for e in range(97,123):
        l2=[]
        for i in s1.split(' '):
            if i.startswith(chr(e)):
                l2.append(i)
        if len(l2)>=1:
            l1.append(l2)
    return l1
print(filter("i want a beautiful girlfriend and lots of money and make my name in sports"))
def dic(s1):
    d1={}
    for e in range(97,123):
        l2=[]
        for i in s1.split(' '):
            if i.startswith(chr(e)):
                l2.append(i)
        if len(l2)>=1:
            d1[chr(e)]=l2
    return d1
print(dic("i want to be greatest of all time in anything"))
"""

def factor(a,b):
    l1=[]
    m=a if a<b else b
    for e in range(1,m+1):
        if a%e==0 and b%e==0:
            l1.append(e)
    return tuple(l1)
print(factor(48,24))