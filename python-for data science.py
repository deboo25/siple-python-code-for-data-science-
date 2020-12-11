#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
from numpy.random import randn


# In[2]:


type(x)


# In[ ]:


x=2.5
x


# In[4]:


type(x)


# In[5]:


x='hello'
x


# In[6]:


type(x)


# In[7]:


x=0
while x<12:
    print ('welcom in the hell')
    x=x+1
print("fuck all this people")


# In[12]:


myListt=['hello','in','the','hell']
for jj in myListt:
    print(jj)


# In[26]:


x=randn()
for j in range(5):
    if x>1:
        ans=('x is greater than one ')
    elif x>=-1:
        ans=('x is between one and negative one  ')
    else:
        ans=('x is less than negative one ')
    print(x)
    print(ans)
    


# In[31]:


n=100
counter=0
for i in randn(n):
    if(i>=-1 and i<=1):
        counter=counter+1
ans=counter/n
print(ans)
    


# In[1]:


l=[1,3,5,'d','mohamed',"hello mother fucker"]
l


# In[3]:


type(l)


# In[4]:


x=[6,7,8,l]
x


# In[53]:


(range(1,25))


# In[54]:


(range(0,100,5))


# In[55]:


#call list  by minus index


# In[17]:


list=[1,2,3,4,5,'ahmed','h','hello']
list


# In[19]:


list[0]


# In[20]:


list[-1]


# In[21]:


list[7]


# In[22]:


list[-8]


# In[23]:


#overwrite


# In[24]:


list[5]="hello in the hell"
list[5]


# In[25]:


list


# In[26]:


#slicing


# In[27]:


letters=['A','B','C','D','E','F','G','H','I','G','K']
letters


# In[28]:


letters[:]


# In[29]:


letters[1:]


# In[31]:


letters[2:9]


# In[32]:


letters[:8]


# In[33]:


#advanced slicing


# In[34]:


letters[::]


# In[35]:


letters[::2]


# In[36]:


letters[1:9:2]


# In[37]:


letters[::-2]


# In[39]:


letters[1:6:-1]


# In[40]:


letters[6:1:-1]


# In[41]:


letters[6:1:-2]


# In[42]:


#tuple 


# In[43]:


t=(1,3,5,'d',"rabbit")
t


# In[44]:


t[1]


# In[45]:


t[4]


# In[46]:


t[2]=4    #syntax error


# In[58]:


import numpy as np #array and numpy


# In[59]:


l=[11,22,553,777.4,34]


# In[60]:


l


# In[62]:


a=np.array(l)
a


# In[66]:


b=np.array([11,44,56,'ahmed',-345]) #all of the data turn to char in array
b


# In[67]:


print(b)


# In[68]:


l.pop()


# In[73]:


l.sort()
l


# In[75]:


b.sort()
print(b)


# In[ ]:





# In[76]:


#slcing array


# In[77]:


w=np.array([223,567,12,87,2356,987,10,1,3,4,5])
w


# In[79]:


q=w[1:4]
q


# In[80]:


q[0]=23#modify of the same array
q


# In[81]:


w


# In[82]:


q[:]=11
q


# In[83]:


w


# In[84]:


#------------------------------------------------------------------------


# In[109]:





# In[108]:





# In[87]:





# In[ ]:





# In[ ]:



    

    


# In[ ]:





# In[ ]:




