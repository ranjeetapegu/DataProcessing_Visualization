#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:28:54 2017

@author: ranjeetapegu
"""

### DataCleansing ###

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

aw_customer= pd.read_csv("AWCustomers.csv",encoding='latin-1')
aw_bikebuyer= pd.read_csv("AW_BikeBuyer.csv",encoding='latin-1')
aw_avespend= pd.read_csv("AW_AveMonthSpend.csv",encoding='latin-1')

# removing duplicate records data
aw_customer= aw_customer.drop_duplicates('CustomerID', keep="first")
aw_bikebuyer= aw_bikebuyer.drop_duplicates('CustomerID', keep="first")
aw_avespend= aw_avespend.drop_duplicates('CustomerID',keep="first")

aw_customer.describe()

#Return the dtypes in this object.
aw_customer.dtypes
# R - Dimension in python
aw_customer.shape
aw_bikebuyer.shape
aw_avespend.shape

#Merging data 

aw_bikecust = pd.merge(aw_customer, aw_bikebuyer,on="CustomerID")
aw_bikecust.head()
aw_cust_bike_avgspe = pd.merge(aw_bikecust, aw_avespend, on="CustomerID")
#Return the dtypes in this object.
aw_cust_bike_avgspe.dtypes

# Dropping Columns
awCust= aw_cust_bike_avgspe.drop(aw_cust_bike_avgspe.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]], 
                                 axis=1)

# Date Conversion 
awCust['t']=pd.Timestamp('1998-01-01')
awCust['BirthDate']    = pd.to_datetime(awCust["BirthDate"],format="%m/%d/%Y")     
awCust['Age']= abs(awCust["t"] - awCust["BirthDate"]).dt.days/365

# Making Category variable
awCust['Education']=awCust['Education'].astype('category')
awCust['Occupation']=awCust['Occupation'].astype('category')
awCust['Gender']=awCust['Gender'].astype('category')
awCust['MaritalStatus']=awCust['MaritalStatus'].astype('category')
awCust['BikeBuyer']=awCust['BikeBuyer'].astype('category')
awCust.dtypes

awCust = awCust.drop(['BirthDate','t'],axis=1)

awCust.dtypes

### Data Visualization

## BOXPLOT


def BB_snsbox(df,col):
    import matplotlib
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.set_style("dark")
    g=sns.boxplot(x="BikeBuyer",y=col,data= df,palette="Set1")
    sns.plt.title('Box plot of ' + col + '\n for BikeBuyer')
    plt.xticks( rotation=90)

fig = plt.figure(figsize = (15,10))
fig.clf()
plt.subplot(331)
BB_snsbox(awCust,'Age')
plt.subplot(332)
BB_snsbox(awCust,'YearlyIncome')
plt.subplot(333)
BB_snsbox(awCust,'NumberCarsOwned')

## VIOLINPLOT
def BB_violin(df, col1,col2):
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set_style("whitegrid")
    g= sns.violinplot(x=col2,y=col1,hue="BikeBuyer", data = awCust,
                       platted="muted", split=True)
    sns.plt.title("voilinplot for BikeBuyer "+ col1 +'-' +  col2)
 
fig = plt.figure(figsize = (15,10))
fig.clf()
plt.subplot(211)    
BB_violin(awCust, "Age","Education")
plt.subplot(212)  
BB_violin(awCust, "YearlyIncome","Occupation")  
 
BB_violin(awCust, "YearlyIncome","Gender")  
BB_violin(awCust, "YearlyIncome","MaritalStatus")  
BB_violin(awCust, "YearlyIncome","HomeOwnerFlag")  
BB_violin(awCust, "YearlyIncome","NumberChildrenAtHome") 
BB_violin(awCust, "Age","MaritalStatus") 


## HISTOGRAM


fig = plt.figure(figsize = (15,10))
plt.subplot(331)
x=awCust["Age"]
sns.distplot(x,bins=20 )
plt.subplot(332)
x=np.log(awCust["Age"])
sns.distplot(x,bins=20 )
plt.subplot(332)
x=np.sqrt(awCust["Age"])
sns.distplot(x,bins=20 )
plt.subplot(333)
x=np.square(awCust["Age"])
sns.distplot(x,bins=20 )



fig = plt.figure(figsize = (15,10))
plt.subplot(331)
x=awCust["YearlyIncome"]
sns.distplot(x,bins=20 )
plt.subplot(332)
x=np.sqrt(awCust["YearlyIncome"])
sns.distplot(x,bins=20 )
plt.subplot(333)
x=np.square(awCust["YearlyIncome"])
sns.distplot(x,bins=20 )
