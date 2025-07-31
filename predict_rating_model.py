import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


df = pd.read_csv("zomato.csv", encoding='latin-1')


df = df.dropna(subset=['Aggregate rating'])


df = df[['Country Code', 'City', 'Cuisines', 'Average Cost for two', 'Price range', 
         'Has Table booking', 'Has Online delivery', 'Votes', 'Aggregate rating']]


df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})


df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')


df['Primary Cuisine'] = df['Cuisines'].apply(lambda x: x.split(',')[0].strip())

le_city = LabelEncoder()
le_cuisine = LabelEncoder()

df['City'] = le_city.fit_transform(df['City'])
df['Primary Cuisine'] = le_cuisine.fit_transform(df['Primary Cuisine'])


X = df[['Country Code', 'City', 'Primary Cuisine', 'Average Cost for two', 
        'Price range', 'Has Table booking', 'Has Online delivery', 'Votes']]
y = df['Aggregate rating']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}


for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"\n{name}")
    print(f"R² Score: {r2:.4f}")
    print(f"Mean Absolute Error: {mae:.4f}")
