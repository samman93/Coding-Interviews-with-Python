def spiralOrder(matrix):
        m = len(matrix)
        if m == 0:
            return[]
        n = len(matrix[0])
        flat_list = []
        a = 0
        b = 0
        c = n - 1
        d = m - 1
        e = m * n #full length of matrix
        bool_loop = True
        while(bool_loop):
            #left to right
            for i in range(a,c+1):
                flat_list.append(matrix[b][i])
                if i == c:
                    b = b + 1
                    break
            if len(flat_list)==m*n:#checking if we should stop while loop or not
                break
            
            #top to bottom
            for j in range(b, d+1):
                flat_list.append(matrix[j][c])
                if j == d:
                    c = c - 1
                    break
            if len(flat_list)==m*n:#checking if we should stop while loop or not
                break
            #right to left
            for i in range(c, a-1, -1):
                flat_list.append(matrix[d][i])
                if i == a:
                    d = d - 1
                    #print("d er value komse")
                    break
            if len(flat_list)==m*n:#checking if we should stop while loop or not
                break
            #bottom to top
            for i in range(d,b-1,-1):
                flat_list.append(matrix[i][a])
                if i == b :
                    a = a + 1
                    break
            if len(flat_list)==m*n:#checking if we should stop while loop or not
                break
        
        return flat_list
    


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#a = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(a))

