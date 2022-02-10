import numpy as np
import Generator as G
import Graph_Generator as Map
import math as m

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

def WierdIdea(Sorted):
    UsedLetters = []                                    # Attempt to avoid loops
    CorrectPaths = []
    Rejects = []
    for index,item in enumerate(Sorted):
        Count = 0                                       # Counts if the point has already been visited
        TestLetters = list(item[1])                     # Turns the two letter path into two list elements
        for letter in UsedLetters:
            if TestLetters[0] ==  letter:               # Checks if letter one is in list
                    Count+=1
            elif TestLetters[1] ==  letter:             # Checks if letter two is in list
                    Count+=1    
            print(letter,Count)
        if Count == 2:
            Rejects.append(item[1])         # DELETABLE debug check
            continue
        CorrectPaths.append(item)
        UsedLetters.extend(TestLetters)
        UsedLetters = list(set(UsedLetters))
    return(CorrectPaths)


def MinimumSpanningTree(Sorted,N):                        # Sorted: list of paths, order of mag
    print(Sorted)    
    UsedLetters = []                                    # Attempt to avoid loops
    CorrectPaths = []                                   # The programs aim
    CorrectEven = []
    CorrectOdd = []
    
    EvenElements = []
    OddElements = []
    
    Rejects = []
    for index,item in enumerate(Sorted):
        if index%2 == 0:
            EvenElements.append(item)
        else:
            OddElements.append(item)
        print (item)                                 
        Count = 0                                       # Counts if the point has already been visited
        TestLetters = list(item[1])                     # Turns the two letter path into two list elements
        print(TestLetters)
        for letter in UsedLetters:
            if TestLetters[0] ==  letter:               # Checks if letter one is in list
                    Count+=1
            elif TestLetters[1] ==  letter:             # Checks if letter two is in list
                    Count+=1    
            print(letter,Count)
        if Count == 2:
            Rejects.append(item[1])         # DELETABLE debug check
            continue
        CorrectPaths.append(item)
        if index % 2 == 0:
            CorrectEven.append(item)
        else:
            CorrectOdd.append(item)
            
        UsedLetters.extend(TestLetters)
        UsedLetters = list(set(UsedLetters))
    EvenCheck = WierdIdea(EvenElements)
    OddCheck = WierdIdea(OddElements)
    Length = len(CorrectPaths)
    if Length < (N-1):
        print(CorrectPaths,"\n")
        CorrectPaths.extend(EvenCheck[m.ceil((Length/2)):m.ceil((N-1)/2)])
        CorrectPaths.extend(OddCheck[m.floor((Length/2)):m.floor((N-1)/2)])
    print(CorrectPaths,UsedLetters,Rejects,"\n",CorrectEven,CorrectOdd,"\n", EvenCheck, OddCheck)
    
    return(CorrectPaths)

# def MinimumSpanningTree(Sorted,N):
#     UsedPairs = []
#     CorrectPaths = []
#     for item in Sorted:
        
        

    
# def Debug(Sorted):
#     prints = 0
#     for item in Sorted:
#         print(item)  
#         prints += 1 
#     print(prints)          
            
        
                    
    
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
Map.GenerateGraph(MinimumSpanningTree(Sorted,N))
#print("\n\n", MinimumSpanningTree(Sorted,N))
#Debug(Sorted)

# ~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary outputs ~~
# ~~~~~~~~~~~~~~~~~~~~~~~

# print(InputMatrix, "\n")
# print(InputList, "\n")
# print(Joined, "\n")
# print (Sorted)
# Map.GenerateGraph()


