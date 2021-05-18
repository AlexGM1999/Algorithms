n = 4
C=[[10,20,12,5],[3,14,9,1],[13,8,6,9],[7,15,6,9]]
X=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
C1=[[10,20,12,5],[3,14,9,1],[13,8,6,9],[7,15,6,9]]


min_element=10**5

for i in range(n):
    for j in range(n):
        if C1[i][j]<min_element:
            min_element=C1[i][j]
    for j in range(n):
        C1[i][j]=C1[i][j]-min_element
    min_element=10**5
min_element=10**5
for j in range(n):
    for i in range(n):
        if C1[i][j]<min_element:
             min_element=C1[i][j]

    for i in range(n):
        C1[i][j]=C1[i][j]-min_element
    min_element=10**5           

marked_zeros=[[n]*2]*n
scratched_zeros=[[n]*2]*n
double_covered_elements=[[n]*2]*n
covered_elements=[[n]*2]*((n*n)-n)
uncovered_elements=[[n]*2]*((n*n)-n)
control_array=[[n]*2]*n
horizontal_lines=[n]*n
vertical_lines=[n]*n
number_marked_zeros=0

while True:
    for i in range(n):
        if marked_zeros[i][0]!=n:
            number_marked_zeros=number_marked_zeros+1
    j_marked_zeros=n
    i_marked_zeros=n
    k=0
    m=0
    counter=0
    complects_zeros_in_rows=0
    complects_zeros_in_column=0
    p=0
    q=0
    r=0
    s=0
    if number_marked_zeros<n:
        j_marked_zeros=n
        i_marked_zeros=n
        k=0
        m=0
        for i in range(n):
            for j in range(n):
                if C1[i][j]==0 and counter==0 and i!=i_marked_zeros and j!=j_marked_zeros:
                    marked_zeros[k]=[i,j]
                    k=k+1
                    counter=counter+1
                    i_marked_zeros=i
                    j_marked_zeros=j

                if C1[i][j]==0 and counter!=0 and i==i_marked_zeros and j!=j_marked_zeros:
                    scratched_zeros[m]=[i,j]
                    m=m+1

                if C1[i][j]==0 and counter!=0 and i!=i_marked_zeros and j==j_marked_zeros:
                    scratched_zeros[m]=[i,j]
                    m=m+1
                if C1[i][j]==0 and counter==0 and i==i_marked_zeros and j!=j_marked_zeros:
                    scratched_zeros[m]=[i,j]
                    m=m+1
                if C1[i][j]==0 and counter==0 and i!=i_marked_zeros and j==j_marked_zeros:
                    scratched_zeros[m]=[i,j]
                    m=m+1
                    
            counter=0

        if i==n-1:
            control_array[0]=marked_zeros[k-1]
            marked_zeros[k-1]=scratched_zeros[m-1]
            scratched_zeros[m-1]=control_array[0]
        for i in range(n):
            if marked_zeros[i][0]==scratched_zeros[i][0] and marked_zeros[i][0]!=n and scratched_zeros[i][0]!=n:
                complects_zeros_in_rows=complects_zeros_in_rows +1
                horizontal_lines[p]=marked_zeros[i][0]
                p=p+1
            if marked_zeros[i][1]==scratched_zeros[i][1] and marked_zeros[i][1]!=n and scratched_zeros[i][1]!=n:
                complects_zeros_in_colunm=complects_zeros_in_column+1
                vertical_lines[q]=marked_zeros[i][1]
                q=q+1
        for i in range(n):
            for j in range(n):
                if horizontal_lines[j]!=n and vertical_lines[i]!=n:
                    double_covered_elements[j]=[horizontal_lines[j],vertical_lines[i]]
        for i in range(n):
            if r<horizontal_lines[0]:
                covered_elements[i]=[i,vertical_lines[0]]
                r=r+1
        for i in range(n):
            for j in range(n):
                if j<vertical_lines[0] and i==horizontal_lines[0]:
                    covered_elements[r]=[i,j]
                    r=r+1
                if j<vertical_lines[0] and i==horizontal_lines[1]:
                    covered_elements[r]=[i,j]
                    r=r+1
        for i in range(n):
            for j in range(n):
                if[i,j]not in double_covered_elements and [i,j] not in covered_elements:
                    uncovered_elements[s]=[i,j]
                    s=s+1

        min_element=10**5
        for i in range(n):
            for j in range(n):
                if [i,j] in uncovered_elements:
                   if C1[i][j]<min_element:
                        min_element=C1[i][j]
        for i in range(n):
            for j in range(n):
                if [i,j]in uncovered_elements:
                     C1[i][j]=C1[i][j]-min_element
                if [i,j] in double_covered_elements:
                     C1[i][j]=C1[i][j]+min_element
    else:
        break
F=0    
for i in range(n):
    for j in range(n):
        if i==marked_zeros[i][0] and j==marked_zeros[i][1]:
            X[i][j]=1
for i in range(n):
    for j in range(n):
        if  i==marked_zeros[i][0] and j==marked_zeros[i][0]:
             F=F+C[i][j]
                                       
                                                                           
print(C1)
print(X)
print(F)                           
                        
            
                
            
        
            
        
            
        
                
        
    
                

                    
                    




