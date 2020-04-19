#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt



v2 = [3, -2]
v3 = [-15 ,4, -3, 2] ##row vectors in order: 2 dimensions, and 3 dimensions



v3Column = np.transpose(v3)


plt.plot([0,v3[0]],[0,v3[2]])
plt.axis((-20, 20, -20, 20))
plt.grid()




## Addition and Substraction of Vectors
v1 = np.array([3, -1])
v2 = np.array([2, 4])

v3 = v1+v2 ## prints 5,3
v4 = v2-v1 ## prints -1, 5

plt.plot([0, v1[0]],[0, v1[1]],'b',label='v1')
plt.plot([0, v2[0]]+v1[0],[0, v2[1]]+v1[1],'r',label='v2')
plt.plot([0, v3[0]],[0, v3[1]],'k',label='v1+v2')
plt.legend()
plt.axis('square')
plt.axis((-6, 6, -6, 6 ))
plt.grid()
plt.show()



## Vector*scalar multiplication
v1 = np.array([3, -1])
l = 2.5
v1m = v1*l ##scaler modulated array([-0.9,  0.3])

plt.plot([0, v1[0]],[0, v1[1]],'b',label='v_1')
plt.plot([0, v1m[0]],[0, v1m[1]],'r:',label='\lambda v_1')

plt.axis('square')
plt.axis((-15,15,-15,15))
plt.grid()
plt.show()




##Vector*Vector Multiplication : Dot Product

v1 = np.array([1,2,3,4,5,6])
v2 = np.array([0, -4, -3, 6, 5,1])

dp = np.dot(v1,v2) ##method1
dp = sum(np.multiply(v1,v2)) ##method2
dp = np.matmul(v1,v2) ## method3

##method4

dp = 0
for i in range(0, len(v1)):
    dp += v1[i]*v2[i]




##Dot Product Properties

##create random vectors
n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

##distributive a(b+c) = ab + ac

result1 = np.dot(a, (b+c))
result2 = np.dot(a,b) + np.dot(a,c)
results = [result1, result2] ##returns same values as result1 and result2 do exactly the same thing


##commutative u.v = v.u
print(np.dot(a,b)) ## same as below
print(np.dot(b,a)) ## same as above



##vector length(magnitutude-norm)
import math as math 

v1= np.array([1,2,3,4,5,6])
length = np.linalg.norm(math.sqrt(np.dot(v1,v1)))







