Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Geospatial Analysis - Task 3
# Author: Your Name
# Description: Visualize restaurants on map, analyze distribution, and check correlation with ratings.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# --------------------------------------
# 1. Load the Dataset
# --------------------------------------
df = pd.read_csv("your_dataset.csv")  # Replace with your file name
print("✅ Dataset Loaded.")
print(df.head())

# --------------------------------------
# 2. Visualize Restaurant Locations on Map
# --------------------------------------
lat_center = df['Latitude'].mean()
lon_center = df['Longitude'].mean()

restaurant_map = folium.Map(location=[lat_center, lon_center], zoom_start=2)

for i, row in df.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row.get('Restaurant Name', ''),
            icon=folium.Icon(color='red', icon='cutlery', prefix='fa')
        ).add_to(restaurant_map)

restaurant_map.save("restaurant_map.html")
print("📍 Restaurant map saved as 'restaurant_map.html'.")

# --------------------------------------
# 3. Distribution of Restaurants by City
# --------------------------------------
plt.figure(figsize=(10, 6))
top_cities = df['City'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index, palette="viridis")
... plt.title("Top 10 Cities with Most Restaurants")
... plt.xlabel("Number of Restaurants")
... plt.ylabel("City")
... plt.tight_layout()
... plt.savefig("city_distribution.png")
... plt.show()
... print("🏙️ City distribution chart displayed and saved as 'city_distribution.png'.")
... 
... # --------------------------------------
... # 4. Distribution of Restaurants by Country
... # --------------------------------------
... plt.figure(figsize=(10, 6))
... top_countries = df['Country'].value_counts().head(10)
... sns.barplot(x=top_countries.values, y=top_countries.index, palette="magma")
... plt.title("Top 10 Countries with Most Restaurants")
... plt.xlabel("Number of Restaurants")
... plt.ylabel("Country")
... plt.tight_layout()
... plt.savefig("country_distribution.png")
... plt.show()
... print("🌍 Country distribution chart displayed and saved as 'country_distribution.png'.")
... 
... # --------------------------------------
... # 5. Correlation Between Location and Rating
... # --------------------------------------
... subset_df = df[['Latitude', 'Longitude', 'Aggregate rating']].dropna()
... correlation = subset_df.corr()
... print("\n📊 Correlation Matrix:\n", correlation)
... 
... plt.figure(figsize=(6, 4))
... sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
... plt.title("Correlation Between Latitude/Longitude and Ratings")
... plt.tight_layout()
... plt.savefig("correlation_heatmap.png")
... plt.show()
... print("📈 Correlation heatmap displayed and saved as 'correlation_heatmap.png'.")
