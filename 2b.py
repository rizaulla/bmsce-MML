#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np 
import sympy as sp
def L(v):
    x,y,z=v
    return np.array([3*x + 2*y - 4*z , x -5*y + 3*z])

s=np.array([[1,1,1],[1,1,0],[1,0,0]])
q=np.array([[1,3],[2,5]])
g=np.array([L(v) for v in s])
g= g.T
q=q.T
a=np.linalg.solve(q,g)
print(a)







# In[26]:


print("Matrix size",'\t',"Multiplication",'\t',"Addition",'\t',"Total",'\t\t',"Time")
for n in range(1,11):
    mul=mul*n+n
    add= add
    total=mul+add
    time=total*(10**-6)
    
    print('\t',n,'\t\t',mul,'\t\t',add,'\t\t',total,'\t\t',time)
    


# In[ ]:


s=np.array([[1,3],[2,5]])
q=np.array([[1,3],[2,5]])


# In[34]:


import numpy as np
def l(v):
    x,y,z=v
    return np.array([3*x+2*y-4*z,x-5*y+3*z])
s=np.array([[1,1,1],[1,1,0],[1,0,0]])
s_prime=np.array([[1,3],[2,5]])
l_s=np.array([l(v) for v in s])
a=np.linalg.solve(s_prime.T,l_s.T)
print(a)


# In[36]:


import numpy as np
s1=([1,1,1],
   [1,1,0],
   [1,0,0])
v1 = ([1,-3,2])
ans = np.linalg.solve(s1,v1)
print(ans)


# In[37]:


f= np.dot(a,ans)
print(f)


# In[39]:


x,y,z=1,-3,2
s=3*x+2*y-4*z,x-5*y+3*z
vector=([1,2],
       [3,5])
ans=np.linalg.solve(vector,s)
print(ans)

