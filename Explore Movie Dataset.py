#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')
movie_data = pd.read_csv("tmdb-movies.csv")


# In[14]:


print(movie_data.dtypes)
print(movie_data.any().isnull())
print(movie_data.describe())


# In[18]:


movie_data = movie_data.dropna(axis=1)
print(movie_data.sample(10))


# In[27]:


selected_columns = movie_data[['id', 'popularity', 'budget', 'runtime', 'vote_average']]

print(selected_columns.head(20))
print(selected_columns[48:50])
print(selected_columns[50:61]['popularity'])


# In[35]:


larger5 =  movie_data[movie_data["popularity"] > 5]
larger5withrelease = movie_data[(movie_data["popularity"] > 5) & (movie_data["release_year"] > 1996)]
print(larger5)
print(larger5withrelease)


# In[43]:


revenue_mean_by_year = movie_data.groupby('release_year').agg({'revenue': 'mean'})
revenue_mean_by_director = movie_data.groupby('director').agg({'popularity': 'mean'}).sort_values(by='popularity', ascending=False)

print(revenue_mean_by_year)
print(revenue_mean_by_director)


# In[46]:


top_20_movies = movie_data.nlargest(20, 'popularity')
plt.figure(figsize=(12, 8))
plt.barh(top_20_movies['original_title'], top_20_movies['popularity'], color='skyblue')
plt.title('Top 20 Movies by Popularity (Bar Chart)')
plt.xlabel('Popularity')
plt.ylabel('Movie Title')
plt.gca().invert_yaxis()  
plt.show()


# In[49]:


movie_data['profit'] = movie_data['revenue'] - movie_data['budget']
profit = movie_data.groupby(['release_year'])['profit']
index = profit.mean().index

plt.figure(figsize=(12, 12))

plt.subplot(3,1,1)
sb.pointplot(x = index, y = profit.mean())
plt.xticks(rotation=90)
plt.title('mean profit')
plt.tight_layout()

plt.subplot(3,1,2)
sb.pointplot(x = index, y = profit.sum())
plt.xticks(rotation=90)
plt.title('sum profit')
plt.tight_layout()

plt.subplot(3,1,3)
sb.pointplot(x = index, y = profit.count())
plt.xticks(rotation=90)
plt.title('sum profit')
plt.tight_layout()

