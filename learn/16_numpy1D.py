import numpy as np
import time 
import sys

import matplotlib.pyplot as plt

a =np.array([0,1,2,3,4])
print(a)
# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print(np.__version__)
print(type(a))
print(a.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:6:2])
c=np.array([100,   1,   2, 300, 400])
select = [0, 2, 3, 4]
d=c[select]
print(d)
c[select]=10000
print(c)
c.size
c.ndim
c.shape


# Plotting functions



u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays

Plotvec1(u, z, v)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.subtract(arr1, arr2)
arr3


# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)
y

# Makeup a numpy array within [-2, 2] and 5 elements

linS=np.linspace(-2, 2, num=5)
print(linS)
linS=np.linspace(-2, 2, num=9)
print(linS)


# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list

y = np.sin(x)

# Plot the result

plt.plot(x, y)


arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
  print(x)


u = np.array([1, 0])
v = np.array([0, 1])
print(u-v)


z = np.array([2, 4])
print(-2*z)

a=np.array([1,2,3,4,5])
b=np.array([1,0,1,0,1])
print(a*b)