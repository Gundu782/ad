import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("your_dataset.csv")  # Replace with your actual filename
print("\n✅ Dataset Loaded Successfully!\n")

# ----------------------------------
# 1. Most Common Price Range
# ----------------------------------
most_common_price_range = df['Price range'].mode()[0]
count = df['Price range'].value_counts().get(most_common_price_range, 0)

print("💰 Most Common Price Range:")
print(f"✔️ Price Range: {most_common_price_range} (Count: {count})\n")

# ----------------------------------
# 2. Average Rating for Each Price Range
# ----------------------------------
avg_rating_by_price = df.groupby('Price range')['Aggregate rating'].mean().reset_index()

print("⭐ Average Rating by Price Range:")
print(avg_rating_by_price, "\n")

# ----------------------------------
# 3. Color with Highest Average Rating
# ----------------------------------
# Group by Price Range and Rating Color
avg_rating_color = df.groupby(['Price range', 'Rating color'])['Aggregate rating'].mean().reset_index()

# Find highest rating for each price range
max_ratings = avg_rating_color.loc[avg_rating_color.groupby('Price range')['Aggregate rating'].idxmax()]

print("🎨 Rating Color with Highest Average Rating in Each Price Range:")
print(max_ratings, "\n")

# ----------------------------------
# Optional: Visualization
# ----------------------------------
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_rating_by_price, x='Price range', y='Aggregate rating', palette='viridis')
plt.title('Average Rating by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.show()
