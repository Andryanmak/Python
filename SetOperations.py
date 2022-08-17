def intersection(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            break;
        elif j==n:
            break;
        elif A[i]<B[j]:
            i=i+1
        elif A[i]>B[j]:
            j=j+1
        elif A[i]==B[j]:
            C.append(A[i])
            i=i+1 
            j=j+1
    return(C)
def setDifference(A,B):
    (m,n)=(len(A),len(B))
    C=[]
    for i in B:
            if i in A:
                C=[k for k in A if k!=i]
                A=C
    return(C)


a=[1,2,7,5,8]
b=[1,2,6,7]
print(intersection(a,b))
print(setDifference(a,b))
