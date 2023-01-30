#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv('C:/Users/DELL/Downloads/archive (9)/housing.csv')


# # Preparing Data for EDA

# In[5]:


df.head()


# In[6]:


#Describing the data

df.describe()


# In[7]:


#Checking info of df

df.info()


# In[9]:


#Checking Data Types
df.dtypes


# In[11]:


#Checking Null Values

df.isna().sum()


# In[12]:


#Checking Percentage of Null Values

df.isna().sum() /len(df) *100


# In[13]:


#Shape of Dataset

df.shape


# In[14]:


#Dropping these Values as null value percentage is less than 1.5%

df.dropna(inplace=True)


# In[17]:


#Outlier Analysis
col=['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']
     
for c in col:
     plt.figure()
     sns.boxplot(df[c])


# In[19]:


#Getting Unique Value Counts

col=['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    
    print('#######')
    print(c)
    print(df[c].value_counts)
    print('#######')


# In[25]:


#Adding one coulmn and converting data into categorical of median_house_value

df['value'] = df['median_house_value']
df['value']=df['value'].astype(str)
df['value'] = df.value.astype('category')


# In[28]:


#Checking the data type

df.dtypes


# # Outlier Analysis

# In[21]:


###Removing Outlier
col=['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    percentile25=df[c].quantile(0.25)
    percentile75=df[c].quantile(0.75)
    iqr=percentile75-percentile25
    upper_limit=percentile75+(1.5*iqr)
    lower_limit=percentile25-(1.5*iqr)
    df=df[df[c]<upper_limit]
    df=df[df[c]>lower_limit]
    plt.figure()
    sns.boxplot(y=c,data=df)


# In[22]:


##Shape of Dataset

df.shape


# # Data Vizualization and Analysis

# In[23]:


col=['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    plt.figure()
    sns.histplot(df[c])


# In[29]:


#Pairplot
sns.pairplot(df)


# In[33]:


# Average value of all numerical Coulmns

col=['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    print('Average value of '+c)
    print(df[c].mean())


# In[34]:


# MEdian value of all numerical Coulmns

col=['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    print('Median value of '+c)
    print(df[c].median())


# In[35]:


# Mode value of all numerical Coulmns

col=['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    print('Mode value of '+c)
    print(df[c].mode())


# In[36]:


# Min value of all numerical Coulmns

col=['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    print('Min value of '+c)
    print(df[c].min())


# In[37]:


# Max value of all numerical Coulmns

col=['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

for c in col:
    print('Max value of '+c)
    print(df[c].max())


# In[41]:


#Mean pric for each total of bedroom

df.groupby('total_bedrooms')['median_house_value'].mean()


# In[42]:


#Mean pric for each number of rooms

df.groupby('total_rooms')['median_house_value'].mean()


# In[43]:


#Mean Price by area type
df.groupby('ocean_proximity')['median_house_value'].mean()


# # Charts by Seaborn

# In[44]:


#Scatter plot

sns.scatterplot(x=df['ocean_proximity'],y=df['median_house_value'])


# In[45]:


#Scatter Chart of Ocean distance and Median income

sns.scatterplot(x=df['ocean_proximity'],y=df['median_income'])


# In[46]:


#Boxplot

sns.barplot(x=df['housing_median_age'],y=df['ocean_proximity'])


# In[50]:


#Count Plot

col=['housing_median_age','households','ocean_proximity']

for c in col:
    plt.figure()
    sns.countplot(df[c])


# In[51]:


#HeatMap
sns.heatmap(df.corr())


# In[52]:


#Distplot

sns.distplot(df['housing_median_age'])


# In[ ]:




