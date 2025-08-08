"""
EcoDrive-Predictor
------------------
Author: [Kashaf Fatima]
Description: Predicts vehicle CO₂ emissions using a simple linear regression model
based on engine size and other vehicle features.
"""

# ===============================
# 1. Import Libraries
# ===============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ===============================
# 2. Load Dataset
# ===============================
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)

# Select relevant features
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

# ===============================
# 3. Initial Exploration
# ===============================
print("Random Sample of Data:\n", df.sample(5))
print("\nDataset Statistics:\n", df.describe())
print("\nColumn Names:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())

# ===============================
# 4. Data Visualization
# ===============================
# Histograms
cdf.hist(figsize=(8, 6))
plt.suptitle("Feature Distributions", fontsize=14)
plt.show()

# Scatter plots
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Fuel Consumption (L/100km)")
plt.ylabel("CO₂ Emissions (g/km)")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine Size (L)")
plt.ylabel("CO₂ Emissions (g/km)")
plt.xlim(0, 10)
plt.show()

plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='red')
plt.xlabel("Cylinders")
plt.ylabel("CO₂ Emissions (g/km)")
plt.show()

# ===============================
# 5. Prepare Training & Testing Data
# ===============================
X = cdf[['ENGINESIZE']].to_numpy()  # Keep as 2D array
y = cdf['CO2EMISSIONS'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# 6. Model Training
# ===============================
regressor = linear_model.LinearRegression()
regressor.fit(X_train, y_train)

print("\nModel Coefficients:", regressor.coef_[0])
print("Model Intercept:", regressor.intercept_)

# ===============================
# 7. Plot Regression Line
# ===============================
plt.scatter(X_train, y_train, color='blue', label="Training Data")
plt.plot(X_train, regressor.predict(X_train), '-r', label="Regression Line")
plt.xlabel("Engine Size (L)")
plt.ylabel("CO₂ Emissions (g/km)")
plt.legend()
plt.show()

# ===============================
# 8. Model Evaluation
# ===============================
y_pred = regressor.predict(X_test)

print("\nModel Performance:")
print("Mean Absolute Error: %.2f" % mean_absolute_error(y_test, y_pred))
print("Mean Squared Error: %.2f" % mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: %.2f" % np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score: %.2f" % r2_score(y_test, y_pred))

