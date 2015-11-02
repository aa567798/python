
# coding: utf-8

# In[4]:

a = [2,"red",3,"blue"]
a


# In[8]:

b = [2,[5,6,"black","white"],"red",3,"blue"]
b[1][2]


# In[15]:

c = [2,[5,6,"black","white",["orange","green",0]],"red",3,"blue"]
c[1][4]


# In[17]:

c = [2,[5,6,"black","white",["orange","green",0]],"red",3,"blue"]
c[1][4][2]


# In[18]:

a = [2,"red",3,"blue"]
a[::-1]


# In[19]:

a = [2,"red",3,"blue"]
a[:-1]


# In[20]:

a = [2,"red",3,"blue"]
a[::1]


# In[21]:

a = [2,"red",3,"blue"]
a[:1]


# In[23]:

a[1]="gray"
a


# In[33]:

color = ["blue","red","yellow","white"]
color


# In[34]:

d = [1,2,3,4,5,6]
color.extend(d)


# In[35]:

color


# In[46]:

color = ["blue","red","yellow","white"]
color


# In[47]:

color.insert(3,"black")
color


# In[48]:

del color[-3]
color


# In[49]:

color.remove("red")
color


# In[51]:

color = ["blue","red","yellow","white","gray"]
color


# In[53]:

color.pop()


# In[54]:

color


# In[56]:

color.pop(1)


# In[57]:

color


# In[59]:

color = ["blue","red","yellow","white","gray"]
color.index("gray")


# In[60]:

"orange" in color


# In[61]:

"blue" in color


# In[65]:

color = ["blue","red","yellow","white","gray","red","white","red"]
color.count("red")


# In[66]:

color.count("white")


# In[68]:

color = ["blue","red","yellow","white","gray","red","white","red"]
color


# In[69]:

','.join(color)


# In[71]:

seperator = " & "
mix = seperator.join(color)
mix


# In[72]:

ccc = mix.split(seperator)
ccc


# In[73]:

sorted_color = sorted(color)
sorted_color


# In[76]:

color.sort()
color


# In[77]:

color.sort(reverse=True)
color


# In[82]:

len(color)


# In[83]:

a = [1,2,3,4,5]
b = a
a[2]="0"
a


# In[84]:

b


# In[87]:

a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 5
a


# In[88]:

b


# In[89]:

c


# In[90]:

d


# In[91]:

empty_tuple = ()
empty_tuple


# In[92]:

one = "guava" ,
one


# In[93]:

fruit_tuple = ("guava","grape","strawberry")
fruit_tuple


# In[94]:

type(fruit_tuple)


# In[95]:

a,b,c = fruit_tuple
a


# In[96]:

b


# In[97]:

c


# In[99]:

a = "guava"
b = "grape"
a,b = b,a
a


# In[100]:

b


# In[101]:

list = ["a","b","c","d"]
tuple(list)

