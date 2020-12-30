#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd

# read facebook json file into a dataframe
df = pd.read_json(r"/Users/EmmanuelAdigun/Documents/emmy/posts/your_posts_1.json")

df.head()


# In[54]:


# Data Cleaning
# Reformat date and remame timestamp column
df.rename(columns={'timestamp':'date'}, inplace=True)

# Remove some unncessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

df.info()
df.head()


# In[55]:


print(df.shape)
df.tail()


# In[56]:


# Monthly post count
df = df.set_index('date')  # Set as Index the date column
post_counts = df['data'].resample('MS').size()  # Resample the data column by month and count the number of occuring posts
post_counts.head(200)


# In[59]:


# set figure size and font size
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)

# set x labels
x_labels = post_counts.index

# create bar plot
sns.barplot(x_labels, post_counts, color="blue")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

# reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

# display the plot
plt.show()


# In[ ]:




