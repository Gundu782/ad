import pandas as pd

# Load your dataset (update the path if necessary)
df = pd.read_csv("zomato.csv", encoding='latin-1')

# ----- Feature 1: Length of restaurant name -----
df['Restaurant_Name_Length'] = df['Restaurant Name'].apply(
    lambda x: len(str(x)))

# ----- Feature 2: Length of address -----
df['Address_Length'] = df['Address'].apply(lambda x: len(str(x)))

# ----- Feature 3: Has Table Booking (binary) -----
df['Has_Table_Booking'] = df['Has Table booking'].apply(
    lambda x: 1 if str(x).lower() == 'yes' else 0)

# ----- Feature 4: Has Online Delivery (binary) -----
df['Has_Online_Delivery'] = df['Has Online delivery'].apply(
    lambda x: 1 if str(x).lower() == 'yes' else 0)

# ----- Optional Feature: Number of Cuisines Listed -----
df['Num_Cuisines'] = df['Cuisines'].apply(
    lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)

# ----- Save the new DataFrame with added features -----
df.to_csv("zomato_with_features.csv", index=False)

# Preview the new columns
print(df[['Restaurant Name', 'Restaurant_Name_Length', 'Address_Length',
          'Has_Table_Booking', 'Has_Online_Delivery', 'Num_Cuisines']].head())
