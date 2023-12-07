#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input())
count=0
for i in range(0,n+1):
    
    values=list(str(i))
    
    
    for j in values:
        if int(j)==1:
            count+=1;
            
print(count)


# In[ ]:




