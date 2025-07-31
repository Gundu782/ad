Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd


df = pd.read_csv('your_dataset.csv')  


print(f"🔎 Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

... print("\n📉 Missing Values in Each Column:\n")
... print(df.isnull().sum())
... 
... 
... import seaborn as sns
... import matplotlib.pyplot as plt
... 
... plt.figure(figsize=(10, 6))
... sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
... plt.title("Missing Values Heatmap")
... plt.show()
... 
... df = df.dropna()  
... 
... print("\n🧾 Data Types Before Conversion:\n")
... print(df.dtypes)
... 
... 
... df['Aggregate rating'] = df['Aggregate rating'].astype(float)
... 
... 
... print("\n✅ Data Types After Conversion:\n")
... print(df.dtypes)
... 
... plt.figure(figsize=(8, 5))
... sns.histplot(df['Aggregate rating'], bins=10, kde=True)
... plt.title("Distribution of Aggregate Rating")
... plt.xlabel("Aggregate Rating")
... plt.ylabel("Frequency")
... plt.show()
... 
... plt.figure(figsize=(8, 5))
... sns.countplot(x='Aggregate rating', data=df)
... plt.title("Class Distribution of Aggregate Rating")
... plt.xlabel("Aggregate Rating")
... plt.ylabel("Count")
... plt.show()
... 
... 
... print("\n📊 Class Distribution:\n")
... print(df['Aggregate rating'].value_counts())
