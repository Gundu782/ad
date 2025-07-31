

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "zomato.csv"  
df = pd.read_csv(file_path, encoding='latin-1')


df['Primary Cuisine'] = df['Cuisines'].astype(str).apply(lambda x: x.split(',')[0].strip())


df = df.dropna(subset=['Primary Cuisine', 'Aggregate rating', 'Votes'])


avg_rating_cuisine = df.groupby('Primary Cuisine')['Aggregate rating'].mean().sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_cuisine.values, y=avg_rating_cuisine.index, palette='Blues_d')
plt.title("Top 15 Cuisines with Highest Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()


total_votes_cuisine = df.groupby('Primary Cuisine')['Votes'].sum().sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 6))
sns.barplot(x=total_votes_cuisine.values, y=total_votes_cuisine.index, palette='Oranges_d')
plt.title("Top 15 Most Popular Cuisines (Based on Total Votes)")
plt.xlabel("Total Votes")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()


top_cuisines = total_votes_cuisine.head(10).index
combined_df = df[df['Primary Cuisine'].isin(top_cuisines)]

grouped = combined_df.groupby('Primary Cuisine').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum'
}).reset_index().sort_values(by='Votes', ascending=False)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=grouped, x='Aggregate rating', y='Votes', hue='Primary Cuisine', s=100)
plt.title("Top 10 Cuisines: Rating vs Votes")
plt.xlabel("Average Rating")
plt.ylabel("Total Votes")
plt.tight_layout()
plt.show()
