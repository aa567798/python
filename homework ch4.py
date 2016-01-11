
# coding: utf-8

# In[6]:

guess_me=7
if guess_me<7:
    print('too low')
elif guess_me>7:
    print('too high')
else:
    print('just right')


# In[8]:

guess_me=7
start=1
while True:
    if start<guess_me:
        print('too low')
    elif start==guess_me:
        print('found it!')
        break
    elif start>guess_me:
        print('oops')
        break
    start += 1


# In[13]:

for value in [3,2,1,0]:
    print(value)


# In[15]:

even=[number for number in range(10) if number % 2 == 0]
even


# In[16]:

squares={key:key*key for key in range(10)}
squares


# In[17]:

odd={number for number in range(10) if number % 2 ==1}
odd


# In[18]:

for thing in ('got %s' % number for number in range(10)):
    print(thing)


# In[19]:

def good():
    return['Harry','Ron','Hermione']
good()


# In[20]:

def get_odds():
    for number in range(1,10,2):
        yield number
for count,number  in  enumerate(get_odds(),1):
    if count==3:
        print("The third odd number is",number)
        break


# In[21]:

def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result
    return new_func
@test
def greeting():
    print("Greetings,Earthing")
greeting()


# In[22]:

titles=['Creature of Habit','Crewel Fate']
plots=['A nun turns into a monster','A haunted yarn shop']
movies=dict(zip(titles,plots))
movies

