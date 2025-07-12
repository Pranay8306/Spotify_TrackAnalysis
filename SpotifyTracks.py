#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")


# In[5]:


# Load the CSV (adjust path if needed)
df = pd.read_csv("spotify_tracks.csv")

# Preview
df.shape, df.head()


# In[7]:


df = pd.read_csv("C:\Users\ragip\OneDrive\Desktop\SpotifyAnalysis\spotify_tracks.csv")

# Preview
df.shape, df.head()


# In[9]:


df = pd.read_csv(r"C:\Users\ragip\OneDrive\Desktop\SpotifyAnalysis\spotify_tracks.csv")

# Preview
df.shape, df.head()


# In[11]:


# Drop rows with missing values in essential columns
df_clean = df.dropna(subset=['track_genre', 'tempo', 'energy', 'valence', 'popularity'])

# Get top 10 genres
top_genres = df_clean['track_genre'].value_counts().nlargest(10).index
df_top_genres = df_clean[df_clean['track_genre'].isin(top_genres)]


# In[13]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df_top_genres, x='track_genre', y='popularity')
plt.xticks(rotation=45)
plt.title("Popularity Distribution Across Top 10 Genres")
plt.tight_layout()
plt.show()


# In[15]:


features = ['popularity', 'danceability', 'energy', 'valence', 'tempo']
corr = df_clean[features].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Audio Features")
plt.tight_layout()
plt.show()


# In[17]:


# Sample 20,000 rows for better rendering
sample_df = df_clean.sample(n=20000, random_state=42)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=sample_df, x='tempo', y='popularity', alpha=0.2)
sns.regplot(data=sample_df, x='tempo', y='popularity', scatter=False, color='red')
plt.title("Tempo vs Popularity")
plt.xlabel("Tempo (BPM)")
plt.ylabel("Popularity")
plt.show()


# In[19]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=sample_df, x='valence', y='popularity', alpha=0.2)
sns.regplot(data=sample_df, x='valence', y='popularity', scatter=False, color='green')
plt.title("Valence vs Popularity")
plt.xlabel("Valence (Positivity)")
plt.ylabel("Popularity")
plt.show()


# In[ ]:




