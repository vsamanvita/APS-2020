#Given a 2D matrix each layer is left rotated 'r' number of times
def matrixRotation(matrix, r):
    for j in range(0,r):
        top=0
        bottom=len(matrix)-1

        left=0
        right=len(matrix[0])-1

        while top<bottom and left<right:
            prev=matrix[top][1]

            for i in range(top,bottom+1):
                cur=matrix[i][left]
                matrix[i][left]=prev
                prev=cur
            left=left+1

            for i in range(left,right+1):
                cur=matrix[bottom][i]
                matrix[bottom][i]=prev
                prev=cur
            bottom=bottom-1

            for i in range(bottom,top-1,-1):
                cur=matrix[i][right]
                matrix[i][right]=prev
                prev=cur
            right=right-1

            for i in range(right,left-2,-1):
                cur=matrix[top][i]
                matrix[top][i]=prev
                prev=cur
            top=top+1

    for i in range(len(matrix)):
        print(*matrix[i])

arr=[[1,2,3],[4,5,6]]
r=3
matrixRotation(arr,r)