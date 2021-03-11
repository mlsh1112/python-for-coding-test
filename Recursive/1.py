def GCD(A,B):    
    temp=A%B
    if temp==0:
        return

    A=B
    B=temp
    print (A,B)
    GCD(A,B)


GCD(192,162)

