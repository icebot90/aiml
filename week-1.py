#dot product without np.dot()
import numpy as np
n=int(input("Enter the size of matrix1: "))
m=int(input("Enter the size of matrix2: "))
if n>m:
    g=n
else:
    g=m
matrix1=np.zeros(g)
matrix2=np.zeros(g)
print("Enter",n,"elements of matrix1")
for i in range(n):
    matrix1[i]=input()
print("Enter",m,"elements of matrix2")
for i in range(m):
    matrix2[i]=input()  
sum=0
for i in range(g):
    sum+=matrix1[i]*matrix2[i]
print("Dot product=",sum)

#dot product with np.dot
import numpy as np
n=int(input("Enter the size of vector1:"))
m=int(input("Enter the size of vector2:"))
vector1=np.zeros(n)
vector2=np.zeros(m)
print("Enter elements of vector1")
for i in range(n):
    vector1=int(input())
print("Enter elements of vector2")
for i in range(m):
    vector2=int(input())
print("Dot product: ",np.dot(vector1,vector2))

#vector magnitude
import numpy as np
n=int(input("Enter the size of vector1: "))
vector=np.zeros(n)
print("Enter",n,"elements of vector")
mag=0
for i in range(n):
    vector[i]=input()
    mag+=vector[i]**2
print("Magnitude of vector",vector,"is:",round(mag**0.5,2))

#Cosine similarity
import numpy as np
n=int(input("Enter the size of vector1:"))
m=int(input("Enter the size of vector2:"))
vector1=np.zeros(n)
vector2=np.zeros(n)
print("Enter",n,"elements of vector1")
mag1=0
for i in range(n):
    vector1[i]=input()
    mag1+=vector1[i]**2
print("Enter",m,"elements of vector2")
mag2=0
for i in range(m):
    vector2[i]=input()
    mag2+=vector2[i]**2
cosine=(np.dot(vector1,vector2))/(mag1**0.5)*(mag2**0.5)
if cosine>0:
    print("Similar direction")
elif cosine==0:
    print("Perpendicular(no similarity)")
else:
    print("Opposite direction")   

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

#matmul using numpy
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
if(matrix1.shape[1]==matrix2.shape[0]):
    multiple=np.matmul(matrix1,matrix2)
    print("Multiplied matrix is:\n",multiple)
else:
    print("Matrix multiplication is not possible")

#Experiment
import numpy as np
from matplotlib import pyplot as plt
print("Enter the 2x2 transformation matrix")
mat=np.zeros([2,2])
for i in range(2):
    mat[i][0],mat[i][1]=map(int,input().split())
n=int(input("How many vectors required: "))
vector=np.zeros([n,2])
print("Enter vector elements in (i-hat j-hat) format")
for i in range(n):
    vector[i][0],vector[i][1]=map(int,input().split())
x=np.zeros(len(vector))
y=np.zeros(len(vector))
u1=vector[:,0]
v1=vector[:,1]
print("Before transformation")
plt.quiver(x,y,u1,v1,angles='xy',scale_units='xy',scale=1)
plt.grid()
plt.show()
new=np.zeros([n,2],dtype=int)
for i in range(n):
    new[i]=np.dot(mat,vector[i])
print("After transformation")
print(new)
u2=new[:,0]
v2=new[:,1]
plt.quiver(x,y,u2,v2,angles='xy',scale_units='xy',scale=1)
plt.grid()
plt.show()