
# coding: utf-8

# In[11]:


def fib1(n):
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()


# In[19]:


def fib2(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result


# In[14]:





# In[22]:




