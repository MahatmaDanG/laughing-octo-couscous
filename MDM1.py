import numpy as np

def RandMatGen (N):
    a = np.random.rand(N, N)                            # set diagonal to 0
    np. fill_diagonal(a, 0)                             # np.tril returns a copy of an array with elements above the k-th diagonal zeroed. 
    M = np.tril(a) + np.tril(a, -1).T                   # lower triangle + a transpose of upper triangle
    M[1,2] = 5
    print(M)
    return (M)

def MatToList(M,N):
    List = []
    X = 0
    while X < N-1:
        for Y in range(X+1,N):
            List.append(M[X,Y])
        X += 1
    return(List)



#def Matrix_Interpret (M):
    


N = 5


InpMatrix = RandMatGen(N)
InpList = MatToList(InpMatrix,N)
print(InpList)
