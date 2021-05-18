def knapSack(W, w, c, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 


    for i in range(n+1): 
        for j in range(W+1): 
            if i==0 or w==0: 
                K[i][j] = 0
            elif w[i-1] <= j: 
                K[i][j] = max(c[i-1] + K[i-1][j-w[i-1]],  K[i-1][j]) 
            else: 
                K[i][j] = K[i-1][j] 
  
    return K[n][W] 


c = [45,50,70,40,30] 
w = [150,160,220,120,80] 
W = 600
n = len(c) 
print(knapSack(W, w,c, n)) 
