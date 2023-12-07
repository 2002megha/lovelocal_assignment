#!/usr/bin/env python
# coding: utf-8

# In[4]:


values=[3,2,3]

n=len(values)//3

count={}
ans=[]
for i in values:
    if i in count.keys():
        count[i]+=1 
    else:
        count[i]=1 



for idx,i in count.items():
    if i>n:
        ans.append(idx)
        
print(ans)
        


# In[ ]:




