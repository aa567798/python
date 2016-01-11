
# coding: utf-8

# In[21]:

days=['monday','tuesdat','wednesday']
fruits=['banana','orange','peach']
drinks=['coffee','tea','beer']
desserts=['cake','ice cream','pie']
for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,",drink",drink,",eat",fruit,",enjoy",dessert)


# In[24]:

def do_nothing():
    pass


# In[25]:

do_nothing()


# In[49]:

def make_a_sound():
    print('quack')
    


# In[50]:

make_a_sound()


# In[53]:

def print_args(*args):
    print('Positional argument tuple:',args)


# In[54]:

print_args()


# In[55]:

print_args(3,2,1,'wait!','uh....')


# In[56]:

def print_more(required1,required2,*args):
    print('need this one:',required1)
    print('need this one too:',required2)
    print('all the rest:',args)


# In[57]:

print_more('cap','gloves','scarf','monocle','mustache max')


# In[58]:

def print_kwargs(**kwargs):
    print('keyword argument:',kwargs)


# In[59]:

print_kwargs(wine='merlot',entree='mutton',dessert='macaroon')


# In[ ]:



