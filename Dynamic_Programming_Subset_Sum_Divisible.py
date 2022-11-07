def subset_divisible ( A  , target ):
    sum = [[0 for j in range(target+1)] for i in range(len(A)+1)]
    parent =[[0 for j in range(target+1)]for i in range(len(A)+1)]
    array =[]
    remainder = []
    array_rem = []
    final_array =[]
    #finding the remainder and storing them in an array also passing the remainder array to subset sum 
    for i in range(len(A)):
        array_rem_append = []
        rem = A[i] % target
        array_rem_append.append(A[i])
        if rem == 0:
            rem = rem + target 
        array_rem_append.append(rem)
        array_rem.append(array_rem_append)
        remainder.append(rem)

    subset,parent = subset_sum(remainder,target,sum,parent)
    #if subset exists find parents else return empty list
    if subset:
        abc = get_subset(len(A),target,parent,array)
    else:
        return []

    for i in range(len(abc)):
        j = 0
        while j < len(array_rem):
            if array_rem[j][1] == abc[i] :
                final_array.append(array_rem[j][0])
                array_rem.pop(j)
                break
            j =j+1
    return final_array

##Referred from professors notes
def subset_sum(A,k,sum,parent):    
    
    sum[0][0]=True
    parent[0][0] = None
    
    for i in range(1,k+1):
        sum[0][i] = False
        parent[0][i] = None
    
    for i in range(1, len(A)+1):
        for j in range(k+1):
            sum[i][j] =sum[i-1][j]
            parent[i][j] =None
            
            if j >=A[i-1] and sum[i-1][j-A[i-1]] == True:
                sum[i][j] =True
                parent[i][j] = j-A[i-1]
#     print(sum)
                
    return sum[len(A)][k],parent

def get_subset(len_A,k,parent,array):
    if k == 0:
        return 
    if parent[len_A][k] ==None:
        get_subset((len_A-1),k,parent,array)
    else:
        get_subset(len_A-1,parent[len_A][k],parent,array)
        array.append(k-parent[len_A][k])        
    return array
