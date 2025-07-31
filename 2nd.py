import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("your_dataset.csv")


print("\n✅ Descriptive Statistics (Numerical Columns):")
print(df.describe())

print("\n📊 Standard Deviation of Numerical Columns:")
print(df.std(numeric_only=True))


categorical_columns = ['Country Code', 'City', 'Cuisines']

for col in categorical_columns:
    print(f"\n🔹 Top values in {col}:")
    print(df[col].value_counts().head(10))

df['Cuisines'] = df['Cuisines'].astype(str) 
all_cuisines = df['Cuisines'].str.split(',').explode().str.strip()
top_cuisines = all_cuisines.value_counts().head(10)

print("\n🍽️ Top 10 Cuisines:")
print(top_cuisines)


top_cuisines.plot(kind='barh', color='skyblue')
plt.title("Top 10 Cuisines")
plt.xlabel("Number of Restaurants")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


top_cities = df['City'].value_counts().head(10)
print("\n🏙️ Top 10 Cities with Most Restaurants:")
print(top_cities)


top_cities.plot(kind='bar', color='orange')
plt.title("Top 10 Cities by Restaurant Count")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
