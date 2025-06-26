import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Load CSV
data = pd.read_csv("data.csv")
print("\nOriginal Data:")
print(data)

# Step 2: Handle missing values
data['age'].fillna(data['age'].mean(), inplace=True)

# Step 3: Encode categorical columns
le = LabelEncoder()
data['gender'] = le.fit_transform(data['gender'])

# Step 4: Display transformed data
print("\nTransformed Data:")
print(data)

# Step 5: Save to new CSV
data.to_csv("processed_data.csv", index=False)
print("\nSaved to 'processed_data.csv'")
