Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("your_dataset.csv")  # Replace with your dataset name
print("\n✅ Dataset Loaded Successfully!\n")

# -------------------------------
# 1. Percentage offering Table Booking
# -------------------------------
table_booking_counts = df['Has Table booking'].value_counts()
total = table_booking_counts.sum()

percent_table_booking = (table_booking_counts.get('Yes', 0) / total) * 100
percent_no_table_booking = (table_booking_counts.get('No', 0) / total) * 100

print("📊 Table Booking Availability:")
print(f"✔️ With Table Booking: {percent_table_booking:.2f}%")
print(f"❌ Without Table Booking: {percent_no_table_booking:.2f}%\n")

# -------------------------------
# 2. Percentage offering Online Delivery
# -------------------------------
online_delivery_counts = df['Is delivering now'].value_counts()
total_delivery = online_delivery_counts.sum()

percent_online_delivery = (online_delivery_counts.get('Yes', 0) / total_delivery) * 100
percent_no_delivery = (online_delivery_counts.get('No', 0) / total_delivery) * 100
... 
... print("🚚 Online Delivery Availability:")
... print(f"✔️ Online Delivery: {percent_online_delivery:.2f}%")
... print(f"❌ No Online Delivery: {percent_no_delivery:.2f}%\n")
... 
... # -------------------------------
... # 3. Average Ratings: Table Booking vs No Table Booking
... # -------------------------------
... avg_rating_table = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
... avg_rating_no_table = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()
... 
... print("⭐ Average Ratings Comparison:")
... print(f"✔️ With Table Booking: {avg_rating_table:.2f}")
... print(f"❌ Without Table Booking: {avg_rating_no_table:.2f}\n")
... 
... # -------------------------------
... # 4. Online Delivery by Price Range
... # -------------------------------
... delivery_by_price = df.groupby(['Price range', 'Is delivering now']).size().unstack().fillna(0)
... 
... # Calculate percentage of delivery in each price range
... delivery_by_price['Delivery %'] = (delivery_by_price.get('Yes', 0) / delivery_by_price.sum(axis=1)) * 100
... 
... print("💰 Online Delivery Availability by Price Range:")
... print(delivery_by_price[['Delivery %']], "\n")
... 
... # -------------------------------
... # Optional: Visualizations
... # -------------------------------
... sns.barplot(x=delivery_by_price.index, y='Delivery %', data=delivery_by_price)
... plt.title("Online Delivery % by Price Range")
... plt.xlabel("Price Range")
... plt.ylabel("Percentage")
... plt.show()
