import numpy as np
import Generator as G

def RandMatGen (N):
    a = np.random.rand(N, N)                            # set diagonal to 0
    np. fill_diagonal(a, 0)                             # np.tril returns a copy of an array with elements above the k-th diagonal zeroed. 
    M = np.tril(a) + np.tril(a, -1).T                   # lower triangle + a transpose of upper triangle
    return (M)



def MatToUTList(M,N):                                   # Converts the matrix to and upper triangular list
    UTList = []
    X = 0                                               
    while X < N-1:                                      # Loops through Rows until penultimate (last row isnt in upper triangular) 

    # Note loop starts from 0 because matrix row 1 is known as 0 in programming  
    
        for Y in range(X+1,N):                          # Loops through the columns for the upper triangular
            UTList.append(M[X,Y])                       # appends item to the list
        X += 1                                          # selects next row
    return(UTList) 


                                     

def CreateTuple(InputList,N):
    CharacterList = G.MatrixPairingList(N)              # Creates the list of letter pairs
    TupleList = list(zip(InputList,CharacterList))      # Joins Inputs and letter pairs in ordered pairs
    return(TupleList)



def CombinedListSort(ProcessingList):
    ProcessingList.sort(key = lambda x: x[0])           # Sorts the combined list by matrix values
    return(ProcessingList)

    
# def MinimumSpanningTree(Sorted):
#     UsedLetters = []
#     CorrectPaths = []
#     for item in Sorted:
#         UsedLetters = list(UsedLetters)                       ####### NOT WORKING #######
#         Count = 0
#         TestLetters = list(item[1])
#         for letter in UsedLetters:
#             if TestLetters[0] ==  letter:
#                     Count+=1
#             elif TestLetters[1] ==  letter:
#                     Count+=1
#         if Count == 2:
#             break
#         CorrectPaths.append(item[1])
#         UsedLetters.extend(TestLetters)
#         UsedLetters = set(UsedLetters)
#     print(CorrectPaths,UsedLetters)
                
            
        
                    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary Value Assignment ~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

N = 5                                                # Matrix size (NxN)


# ~~~~~~~~~~~~~~~~~
# ~~ Running Hub ~~
# ~~~~~~~~~~~~~~~~~

InputMatrix = RandMatGen(N)                             # Makes the input matrix
InputList = MatToUTList(InputMatrix,N)                  # Turns input matrix into an upper triangular list
Joined = CreateTuple(InputList, N)                      # Pairs the upper triangular list with letter pairs
Sorted = CombinedListSort(Joined)                       # Sorts the combined list
# MinimumSpanningTree(Sorted)

# ~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary outputs ~~
# ~~~~~~~~~~~~~~~~~~~~~~~

print(InputMatrix, "\n")
print(InputList, "\n")
print(Joined, "\n")
print (Sorted)


