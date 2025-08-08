# EcoDrive-Predictor
A machine learning regression model that predicts vehicle CO₂ emissions based on engine size, cylinders, fuel consumption, and related features.

---

##  Overview

EcoDrive-Predictor demonstrates the full machine learning pipeline: from data loading and exploratory data analysis (EDA) to model training and evaluation. Built with **Python**, **Pandas**, **NumPy**, **Matplotlib**, and **Scikit-learn**, it offers insight into how vehicle parameters affect emissions.

---

##  Dataset

Data source: [FuelConsumptionCo2.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv)

**Key Features Used:**
- `ENGINESIZE` – Engine displacement (liters)  
- `CYLINDERS` – Number of engine cylinders  
- `FUELCONSUMPTION_COMB` – Combined fuel consumption (L/100 km)  
- `CO2EMISSIONS` – CO₂ emissions in g/km  

---

##  Features & Functionality

- Data loading and cleansing using Pandas  
- EDA with histograms and scatter plots in Matplotlib  
- Simple linear regression model using Scikit-learn  
- Performance evaluation using MAE, MSE, RMSE, and R² metrics  

---

## ​​​ Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kashaffatimaaa/EcoDrive-Predictor.git
cd EcoDrive-Predictor

Install dependencies:

bash
pip install pandas numpy matplotlib scikit-learn jupyter

Run the notebook:
jupyter notebook EcoDrive-Predictor.ipynb

Then open EcoDrive-Predictor.ipynb and run all cells.

The model shows a clear linear relationship between engine size and CO₂ emissions.
Typical evaluation metrics (values may vary):

R² Score: ~0.85—0.90

Mean Absolute Error: 24.10

Mean Squared Error: 985.94

Root Mean Squared Error: 31.40

Sample Data:


 MODELYEAR       MAKE                MODEL             VEHICLECLASS
915       2014        RAM         1500 4X4 FFV  PICKUP TRUCK - STANDARD
316       2014      DODGE                 DART                 MID-SIZE
886       2014    PORSCHE              BOXSTER               TWO-SEATER
707       2014      MAZDA  MAZDA3 4-DOOR (SIL)                  COMPACT
241       2014  CHEVROLET            SILVERADO  PICKUP TRUCK - STANDARD


---

##  Visual Results

1. Feature Distributions:
   
<img width="561" height="435" alt="image" src="https://github.com/user-attachments/assets/c767b7cd-c363-4d18-aed7-a59e4ae1b5f4" />

2. CO₂ Emissions vs Fuel Consumption (Combined):

<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/21629b97-8fa6-493a-9585-17ea3225c539" />

3. CO₂ Emissions vs Engine Size

<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/41ff4151-be6a-4a9e-9883-6c611d90865f" />

4. CO₂ Emissions vs Cylinders

<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/559cb1d0-eb80-48d0-80ec-843e1a5adf46" />

5. Regression Line Fit — CO₂ Emissions vs Engine Size

<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/42d2fbef-af08-4f6b-9436-d98cbac7c171" />





