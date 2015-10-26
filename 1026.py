
# coding: utf-8

# In[3]:

a = 7
print(a)


# In[4]:

b = a
print(b)


# In[7]:

9 / 5


# In[8]:

a = 50
a


# In[9]:

a - 3 


# In[10]:

a = 90
a -=4
a


# In[11]:

a = a * 2
a


# In[12]:

a = 13
a //= 4
a


# In[13]:

float(2)


# In[14]:

int(-23)


# In[15]:

int(98.5)


# In[16]:

int(13ejirjeirjerd)


# In[17]:

52.7 + 3


# In[18]:

____


# In[19]:

5 + 9


# In[20]:

100 + 3


# In[21]:

100000000000000000000333333333333 - 1


# In[22]:

5 / 0


# In[23]:

"中文"


# In[24]:

'''我是中文'''


# In[25]:

'哈哈'


# In[26]:

joke = "有一天小明說小美妳美爆了 然後小美就爆了"
joke


# In[27]:

true + 5


# In[28]:

True + 5 


# In[29]:

False + 0


# In[31]:

type(rrrrrrrrr)


# In[45]:

type(joke)


# In[46]:

bottles = 99


# In[47]:

base = " "


# In[48]:

base +='現有存量:'


# In[49]:

base += str(bottles)


# In[50]:

base


# In[52]:

address = '宇宙,\n太陽系,\n地球,\n台灣,\n台北市'


# In[53]:

print(address)


# In[54]:

address = "宇宙,\t太陽系,\t地球,\t台灣,\t台北市"


# In[55]:

print(address)


# In[5]:

address = "宇宙,\\太陽系,\\地球,\\台灣,\\台北市"


# In[57]:

print(address)


# In[59]:

address = "我的地址\"宇宙,太陽系,地球,台灣,台北市\""


# In[62]:

print(address)


# In[63]:

print("感冒了" + "好想睡覺")


# In[64]:

East = '東東東東東東東東東東東東'


# In[65]:

West = '西'


# In[71]:

print(East * 10 + West * 100)


# In[74]:

QAQ = "QWERTYUIOPLKJHGFDSAZXCVBNM"
QAQ[:]


# In[75]:

QAQ[5:]


# In[76]:

QAQ[:5]


# In[79]:

QAQ[4:10]


# In[80]:

QAQ[-10:]


# In[87]:

name = ("姊姊討厭妹妹妹妹愛姊姊")
name.replace('妹','姊')


# In[7]:

address = "宇宙,\\太陽系,\\地球,\\台灣,\\台北市"


# In[8]:

len(address)


# In[11]:

wow = "遲到,發呆,閒晃,18人撤銷公務員資格"
wow.split(',')


# In[19]:

burned = "rinse,undress,soak,cover,send"
burned.split(',')


# In[24]:

news = "財政部長張盛和今天表示，房市萎縮是因房價漲到高點自然下滑的影響；對於房仲業憂心明年恐爆裁員潮，張盛和說，國內房仲業者「太多了」，「買房子不是買礦泉水」，各國也沒有像台灣這樣，房仲業跟7-11一樣多。"
print(news)


# In[25]:

news[3:15]


# In[26]:

len(news)


# In[29]:

news.startswith('經濟部長')


# In[30]:

news.endswith('一樣多。')


# In[55]:

import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/xajh/029.htm")
response.encoding = "big5"
book1 = response.text


# In[54]:

word2 = '令狐沖'
book1.count(word2)


# In[ ]:

list("google")


# In[ ]:

a_tuple = ('ready','fire','aim')
list(a_tuple)


# In[ ]:

a = [[1,"jerry",2,"吳老師"],"NTUST"]
a[0][3]


# In[ ]:



