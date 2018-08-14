def minPathSum(grid):
    weights=[[999999999 for x in range(len(grid[0]))] for y in range(len(grid))]
    weights[0][0]=grid[0][0]
    for i in range(1,len(grid)):
        weights[i][0]=weights[i-1][0]+grid[i][0]
    for i in range(1,len(grid[0])):
        weights[0][i]=weights[0][i-1]+grid[0][i]
        
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            weights[i][j]=min([weights[i-1][j]+grid[i][j],weights[i][j-1]+grid[i][j]])
    
    return weights[-1][-1]