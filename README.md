# EcoDrive-Predictor
Overview

This project builds a regression model to predict CO₂ emissions based on vehicle features such as engine size, number of cylinders, and fuel consumption. The dataset was analyzed using Python, Pandas, Matplotlib, and scikit-learn, with visualization of relationships between variables and model evaluation.

Features
Data cleaning and preprocessing using Pandas

Exploratory Data Analysis (EDA) with Matplotlib

Simple linear regression and multiple regression models

Evaluation metrics for model performance

Dataset
Data source: [FuelConsumptionCo2.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv)

**Key Features Used:**
- `ENGINESIZE` – Engine displacement (liters)  

ENGINESIZE – Engine displacement (L)

CYLINDERS – Number of cylinders

FUELCONSUMPTION_COMB – Combined fuel consumption (L/100 km)

CO2EMISSIONS – Emissions in grams/km

Example Visualization
Scatter plots showing the relationship between:

Engine Size vs CO₂ Emissions

Cylinders vs CO₂ Emissions

Fuel Consumption vs CO₂ Emissions

How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Kashaffatimaaa/EcoDrive-Predictor.git
Install required libraries:

bash
Copy
Edit
pip install pandas matplotlib scikit-learn
Open the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook
Run all cells to see the analysis and model results.

Results
The model shows a strong positive correlation between engine size and CO₂ emissions.

Multiple regression improves prediction accuracy by combining several features.

License
This project is open-source and available under the MIT License.


