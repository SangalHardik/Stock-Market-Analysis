#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


# In[57]:


google.to_csv('Google_stock.csv')


# In[58]:


start = datetime.datetime(2021,1,1) #1st Jan
end   = datetime.datetime(2022,5,1 )#1st May


# In[59]:


google = web.DataReader("GOOGL",'yahoo',start,end)

#GOOGL is the name of the stock
#yahoo is form where we seached  
#followed by start and end date


# In[60]:


#google stock data
google.head()


# In[61]:


#Stock price visualization
google['Open'].plot(label = 'GOOGL Open price')
google['Close'].plot(label = 'GOOGL Close price')
google['High'].plot(label = 'GOOGL High price')
google['Low'].plot(label = 'GOOGL Low price')
plt.legend()
plt.title('Google Stock Price')
plt.ylabel('Stock Price')
plt.show()


# In[62]:


#Volume traded
google['Volume'].plot()
plt.title('Volume Traded')


# In[63]:


#to find max
google['Volume'].argmax()


# In[64]:


google.iloc[[google['Volume'].argmax()]]


# In[65]:


#Market cap
google['Total Traded']=google['Open']*google['Volume']


# In[66]:


google.head()


# In[67]:


google['Total Traded'].plot()


# In[68]:


google['Total Traded'].argmax()


# In[69]:


google.iloc[[google['Total Traded'].argmax()]]


# In[70]:


#moving Average
google['Open'].plot()
google['MA10']=google['Open'].rolling(50).mean()
google['MA10'].plot(label='MA10')


# In[71]:


#Daily Percentage Change
#rt=pt/pt-1 -1
google['Returns']=(google['Close']/google['Close'].shift(1))-1


# In[72]:


google.head()


# In[73]:


google['Returns'].argmax()


# In[74]:


google.iloc[[google['Returns'].argmax()]]


# In[ ]:




