#Subscribed on YouTube by AMRITSARI KING. Don't have facebook id.
def findCandidate(A): 
    maj_index = 0
    count = 1
    for i in range(len(A)): 
        if A[maj_index] == A[i]: 
            count += 1
        else: 
            count -= 1
        if count == 0: 
            maj_index = i 
            count = 1
    return A[maj_index] 
  

def isMajority(A, cand): 
    count = 0
    for i in range(len(A)): 
        if A[i] == cand: 
            count += 1
    if count > len(A)/2: 
        return True
    else: 
        return False
  

def printMajority(A): 
    # Find the candidate for Majority 
    cand = findCandidate(A) 
      
    # Print the candidate if it is Majority 
    if isMajority(A, cand) == True: 
        print(cand) 
    else: 
        print("No Majority Element") 
  

A = [1, 3, 3, 1, 2] 
printMajority(A)
