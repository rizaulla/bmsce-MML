#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np 
def L(v):
    x,y,z=v
    return np.array([3*x+2*y-4*z,x-5*y+3*z])

s=np.array([[1,1,1],[1,1,0],[1,0,0]])
q=np.array([[1,3],[2,5]])
g=np.array([L(v) for v in s])
g= g.T
a=np.linalg.solve(q,g)
print(a)


# In[ ]:




