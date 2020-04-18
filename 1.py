#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[11]:


v2 = [3, -2]
v3 = [-15 ,4, -3, 2] ##row vectors in order: 2 dimensions, and 3 dimensions


# In[12]:


v3Column = np.transpose(v3)


# In[17]:


plt.plot([0,v3[0]],[0,v3[2]])
plt.axis((-20, 20, -20, 20))
plt.grid()


# In[21]:


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


# In[23]:


## Vector-scalar multiplication
v1 = np.array([3, -1])
l = -.3
v1m = v1*l ##scaler modulated array([-0.9,  0.3])

plt.plot([0, v1[0]],[0, v1[1]],'b',label='v_1')
plt.plot([0, v1m[0]],[0, v1m[1]],'r:',label='\lambda v_1')

plt.axis('square')
plt.axis((-3,3,-3,3))
plt.grid()
plt.show()






