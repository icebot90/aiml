# #vector addition
# import numpy as np
# arr1=np.array([[1],[2]])
# arr2=np.array([[7],[3]])
# print(arr1+arr2)

# #scalar multiplication
# print(2*arr1)

# #spanning
# import random
# arr3=arr1.copy()
# arr4=arr2.copy()
# for i in range(1,10):
#     print(random.randint(0,11)*arr3+random.randint(0,11)*arr4)

#linear transformation
# import numpy as np
# matrix=np.array([[1,3],[2,4]])
# print(matrix)
# x=np.array([1,2])
# i=0
# for col in matrix:
#     matrix[i]=x[i]*col
#     i+=1
# print(matrix)

#matrix multiplication
import numpy as np
n=int(input("Enter the size of the array1:"))
matrix1=np.zeros([n,n],dtype=int)
m=int(input("Enter the size of array2:"))
matrix2=np.zeros([m,m],dtype=int)
multiple=np.zeros([n,n],dtype=int)
print("Enter elements for matrix 1:")
for i in range(n):
    matrix1[i][0],matrix1[i][1],matrix1[i][2]=map(int,input().split())
print("Matrix1:\n",matrix1)
print("Enter elements for matrix 2:")
for i in range(n):
    matrix2[i][0],matrix2[i][1],matrix2[i][2]=map(int,input().split())
print("Matrix2:\n",matrix2)
for i in range(n):
    for j in range(n):
        for k in range(n):
            multiple[i][j]+=matrix1[i][k]*matrix2[k][j]
print("Multiplied matrix:\n",multiple)