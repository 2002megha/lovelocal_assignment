#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string=input()
str1=string[::-1]
count=0
for i in str1:
    if i==" ":
        break 
    else:
        count+=1
print(count)

