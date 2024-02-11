#!/usr/bin/env python
# coding: utf-8

# # Practice Session

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


weather_df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Weather.csv")
weather_df


# In[25]:


weather_df = pd.DataFrame({'City':['London','London','London','London','Paris','Paris','Paris','Paris'],
                           'Season':['Fall','Winter','Spring','Summer','Fall','Winter','Spring','Summer'],
                           'Temperature':[68,94,103,21,68,94,103,21]})
weather_df


# In[22]:


#Q2 Generate and save a dataframe with all of the columns: (a) day, (b) month and 
#(c) year between the current day from the independence day of India.


# In[20]:


start_date = datetime(1947, 8, 15)  
end_date = datetime.now()

date_df = pd.date_range(start=start_date, end=end_date)


# In[21]:


df = pd.DataFrame(date_df, columns=['date'])

df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

print(df)


# In[ ]:


# Write a python code for finding out top K frequent item from a list.
# input : [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1],      2    

# output :  [1, 2]


# In[23]:


from collections import Counter

i = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
k = 2

def top_k(nums, k):
    counts = Counter(nums)
    return [item for item, _ in counts.most_common(k)]

op = top_k(i, k)
print(op)


# In[ ]:


# Q4. Write a sql query to retrieve the top 3 highest-mark_achiever students from the a table, along with their marks.

use nishadb;

-- Write a sql query to retrieve the top 3 highest-mark_achiever students from the a table, along with their marks.

SELECT st_id, stu_name, marks_achieved
FROM stud
ORDER BY marks_achieved DESC
LIMIT 3;


# In[ ]:


Q4.
#-- Divide a student table having their marks into 4 equal marks groups (quartiles) and show their details.

SELECT stu_name, marks_achieved,
NTILE(4) OVER (ORDER BY marks_achieved) AS quartile
FROM stud;

