
# coding: utf-8

# In[1]:

empty_dict = {}
empty_dict


# In[2]:

haha = {"a":"apple","b":"banana","c":"cat"}
haha


# In[3]:

haha = {"b":"banana","c":"cat","a":"apple"}
haha


# In[4]:

kk = [["e","elephant"],["d","dog"],["f","fruit"]]
dict(kk)


# In[5]:

b = {"書":"book","蘋果":"apple","車":"car"}
b


# In[6]:

b["書"]


# In[7]:

kk = {"e":"elephant","d":"dog","f":"fruit"}
haha = {"b":"banana","c":"cat","a":"apple"}
kk.update(haha)
kk


# In[8]:

del kk["e"]
kk


# In[9]:

"a" in kk


# In[10]:

"e" in kk


# In[11]:

kk.get("f")


# In[12]:

kk.get("h","wowowowow")


# In[13]:

kk = {"e":"elephant","d":"dog","f":"fruit","b":"banana","c":"cat","a":"apple"}
kk.keys()


# In[14]:

kk.values()


# In[15]:

list(kk.values())


# In[16]:

list(kk.items())


# In[18]:

empty_set = set()
empty_set


# In[20]:

set("happy")


# In[21]:

set(["water","colder","flyer"])


# In[33]:

set(("water","colder","flyer"))


# In[39]:

a = [1,1,3,4]
set(a)
b = 'len(set(a))'
b


# In[ ]:



