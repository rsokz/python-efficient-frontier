#!/usr/bin/env python
# coding: utf-8

# Efficient Frontier

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

assets = ['WMT', 'FB']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']


# In[2]:


log_returns = np.log(pf_data / pf_data.shift(1))

num_assets = len(assets)

weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# Expected Portfolio Return:

# In[3]:


np.sum(weights * log_returns.mean()) * 250


# Expected Portfolio Variance:

# In[4]:


np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))


# Expected Portfolio Volatility:

# In[5]:


np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))


# ***

# 1)	Create two empty lists.

# In[6]:


pf_returns = []
pf_volatilities = []


# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.

# In[7]:


for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pf_returns, pf_volatilities


# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites.

# In[8]:


pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)

pf_returns, pf_volatilities


# In[9]:


portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_volatilities})


# In[10]:


portfolios.head()

portfolios.tail()
# Plot the data from the portfolios dictionary on a graph. The x-axis represents the volatility data from the portfolios dictionary and the y-axis represents the data about rates of return.

# In[11]:


portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')


# ******

# Adding a 3rd stock to the Markowitz Efficient (British Petroleum (‘BP’)).
# 

# In[12]:


assets = ['WMT', 'FB', 'BP']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']


# In[13]:


pf_data.head()


# In[14]:


log_returns = np.log(pf_data / pf_data.shift(1))


# In[15]:


num_assets = len(assets)
num_assets


# In[16]:


weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# In[17]:


weights[0] + weights[1] + weights[2]


# Expected Portfolio Return:

# In[18]:


np.sum(weights * log_returns.mean()) * 250


# Expected Portfolio Variance:

# In[19]:


np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))


# Expected Portfolio Volatility:

# In[20]:


np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))


# *****

# In[21]:


pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities


# In[22]:


portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})


# In[23]:


portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')

