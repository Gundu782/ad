Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... 
... import pandas as pd
... import matplotlib.pyplot as plt
... import seaborn as sns
... 
... 
... file_path = "zomato.csv"  
... df = pd.read_csv(file_path, encoding='latin-1')
... 
... 
... sns.set(style="whitegrid")
... 
... 
... plt.figure(figsize=(8, 5))
... sns.histplot(df['Aggregate rating'].dropna(), bins=20, kde=True, color='skyblue')
... plt.title('Distribution of Aggregate Ratings')
... plt.xlabel('Rating')
... plt.ylabel('Count')
... plt.tight_layout()
... plt.show()
... 
... 
... plt.figure(figsize=(8, 5))
... rating_counts = df['Aggregate rating'].value_counts().sort_index()
... sns.barplot(x=rating_counts.index, y=rating_counts.values, palette='magma')
... plt.title('Rating Frequencies')
... plt.xlabel('Rating')
... plt.ylabel('Number of Restaurants')
... plt.tight_layout()
... plt.show()
... 
... 
... df['Primary Cuisine'] = df['Cuisines'].astype(str).apply(lambda x: x.split(',')[0])
... top_cuisines = df['Primary Cuisine'].value_counts().head(10).index
... cuisine_df = df[df['Primary Cuisine'].isin(top_cuisines)]
... 
... plt.figure(figsize=(10, 6))
... sns.barplot(x='Aggregate rating', y='Primary Cuisine', data=cuisine_df, estimator='mean', ci=None, palette='viridis')
... plt.title('Average Rating by Top Cuisines')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine')
plt.tight_layout()
plt.show()


top_cities = df['City'].value_counts().head(10).index
city_df = df[df['City'].isin(top_cities)]

plt.figure(figsize=(10, 6))
sns.barplot(x='Aggregate rating', y='City', data=city_df, estimator='mean', ci=None, palette='coolwarm')
plt.title('Average Rating by Top Cities')
plt.xlabel('Average Rating')
plt.ylabel('City')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Aggregate rating', y='Votes', hue='Has Online delivery', alpha=0.6)
plt.title('Votes vs Rating (colored by Online Delivery)')
plt.xlabel('Aggregate Rating')
plt.ylabel('Votes')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Price range', y='Aggregate rating', palette='Set2')
plt.title('Price Range vs Rating')
plt.xlabel('Price Range')
plt.ylabel('Aggregate Rating')
plt.tight_layout()
plt.show()
