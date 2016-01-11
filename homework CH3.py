
# coding: utf-8

# In[1]:

years_list = [1995,1996,1997,1998,1999,2000]


# In[2]:

years_list[3]


# In[3]:

years_list[-1]


# In[1]:

things = ["mozzarella", "cinderella", "salmonella"]
things


# In[2]:

things[1].capitalize()


# In[3]:

things[0] = things[0].upper()


# In[4]:


things


# In[5]:

things.remove("salmonella")
things


# In[6]:

suprise = ['Groucho', 'Chico', 'Harpo']
suprise


# In[7]:

suprise[-1] = suprise[-1].lower()
suprise


# In[10]:

suprise[-1] = suprise[-1][::-1]
suprise


# In[11]:

suprise[-1].capitalize()


# In[12]:

e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
e2f


# In[13]:

e2f['walrus']


# In[14]:

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
f2e


# In[15]:

f2e['chien']


# In[16]:

set(e2f.keys())


# In[17]:

life = {
    'animals':{
        'cat':[
            'Henri','Grumpy','Lucy'
            ],
        'octopi':{},
        'emus':{},
        },
    'plants':{},
    'other':{}
    }
life


# In[18]:

print(life.keys())


# In[20]:

print(life['animals'].keys())


# In[22]:

print(life['animals']['cat'])

