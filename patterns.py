def patter(n):
    row=n+1
    for i in range(1,row):#for(i=1;i<n+1;i++)
        for j in range(1,i+1):
            print("*",end=" ")
        print("")
def patter1(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print("")
def patter2(n):
    for i in range(1,n+1):
        for j in range(0,n+1-i):
            print("*",end=" ")
        print("")
def patter3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("")
def patter4(n):
    for i in range(0, 2*n):
        cols=i>n and 2*n-i or i
        if i>n:
            for j in range(0, cols):
                print("*", end=" ")
        else:
            for j in range(i):
                print("*",end=" ")
        print("")

def patter5(n):
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k=k-2
        for j in range(i+1):
            print("*",end=" ")
        print(" ")
def patter6(n):
    for i in range(n):
        space=n-i
        for j in range(space):
            print(end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print(" ")
def patter7(n):
    for i in range(2*n):
        cols=i>n and 2*n-i or i
        space=n-cols
        for j in range(space):
            print(end=" ")
        for j in range(cols):
            print("*",end=" ")
        print(" ")
def patter8(n):
    for i in reversed(range(n)):
        space=n-i
        for j in range(space):
            print(end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print(" ")
def patter9(n):
    for i in range(n):
        space=n-i
        for j in range(space):
            print(end=" ")
        c=97
        for j in range(i+1):
            print(chr(c),end=" ")
            c+=1
        print(" ")
n=5
#patter(n)
#patter1(n)
#patter2(n)
#patter3(n)
#patter4(n)
#patter5(n)
patter9(n)