def get_max_sbstr (s , c1 , c2 ):
    
    #creating a substring for performing operation for matrix 
    substring =c1+c2
    new_string1 = c1 + s
    #calling 2 times because checking if adding c1 giving more or c2 giving more
    get_how_many_substring_c1 = get_how_many_string(new_string1,substring)
    new_string2 = s + c2
    get_how_many_substring_c2 = get_how_many_string(new_string2,substring)
    
    if get_how_many_substring_c1 > get_how_many_substring_c2:
        return get_how_many_substring_c1
    else:
        return get_how_many_substring_c2
#referred form professors code for longest subsequence and modified for getting the values
def get_how_many_string(s,substring):
    
    matrix = [[0 for i in range(len(substring)+1)]for i in range(len(s)+1)]
    
    for i in range(len(matrix)):
        matrix[i][0] = 1
    
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if s[i-1] == substring[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
        
    return matrix[-1][-1]