
# coding: utf-8

# In[40]:

import pandas

series = pandas.Series([140, 160, 180], index=['王小雪', '梁大釗', '陳運運'])
df = pandas.DataFrame({
        '身高': series,
        '學校': '台灣科技大學'
    })


# In[42]:

series


# In[43]:

df


# In[7]:

list_ = ['✈', 9**3,  "ob'_'bv", {}]
print(list_)
print(list_[2:])


# In[11]:

series = pandas.Series([1, 2, 3, 4, 5])


# In[14]:

series[3]


# In[16]:

series[2:]


# In[19]:

series[1] = 1
series


# In[21]:

成績 = pandas.Series([15, 20, 30, 10, 60])


# In[22]:

成績 > 60


# In[23]:

成績[成績 > 60]


# In[24]:

成績 = pandas.Series([15, 20, 30, 10, 60])


# In[25]:

print(成績+10)
print(成績*0.3)
print(成績**0.5*10)


# In[34]:

pd=pandas


# In[35]:

macPrice = pd.Series([31900, 7488, 112800, 999, 1549], index=['台灣', '香港', '日本', '美國', '澳洲'])


# In[36]:

exchangeRate = pd.Series([32.45500, 4.08000, 23.28000, 0.25970, 1], index=['美國', '香港', '澳洲', '日本', '台灣'])


# In[37]:

macPriceInTW = macPrice * exchangeRate


# In[38]:

macPriceInTW['日本'] *= 1.08


# In[39]:

macPriceInTW


# In[45]:

macIndex = pd.DataFrame({
        '原始價格': macAirPrice,
        '外幣：台幣': exchangeRate,
        '台幣：外幣': 1 / exchangeRate,
        '實際價格': macAirPriceInTWD # macAirPrice * exchangeRate
    })


# In[47]:

macIndex


# In[48]:

airPollution = pd.read_csv('http://opendata.epa.gov.tw/ws/Data/AQX/?format=csv&ndctype=CSV&ndcnid=6074', encoding="utf-8-sig")


# In[49]:

airPollution.head()


# In[50]:

airPollution.dtypes


# In[51]:

macIndex


# In[52]:

macIndex['台幣：外幣']


# In[54]:

macIndex[['台幣：外幣', '原始價格']]


# In[57]:

macIndex['人均GDP'] = pd.Series({
    '美國': 54596.65,
    '日本': 37389.79,
    '台灣': 45853.74,
    '香港': 54722.12,
    '澳洲': 46433.30
})


# In[58]:

macIndex


# In[59]:

macIndex.plot(x = '人均GDP', y='實際價格', kind='scatter')


# In[60]:


macIndex[0:2]


# In[61]:

macIndex.ix['台灣':'日本']


# In[62]:

macIndex.ix[['台灣', '日本']]


# In[63]:


airPollution.head()


# In[64]:

airPollution[airPollution['SiteName'] == '金門']


# In[65]:

airPollution[(airPollution['SO2'] > 5) | (airPollution['PM2.5'] > 50)].head()


# In[66]:

airPollution.head()


# In[69]:

airPollution = airPollution.set_index('SiteName')


# In[70]:

airPollution.head()


# In[71]:

airPollution.ix['金門']


# In[ ]:



