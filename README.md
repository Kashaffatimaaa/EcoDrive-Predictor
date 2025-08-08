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
Copy
Edit
pip install pandas numpy matplotlib scikit-learn jupyter
Run the notebook:

bash
Copy
Edit
jupyter notebook
Then open EcoDrive-Predictor.ipynb and run all cells.

Results
The model shows a clear linear relationship between engine size and CO₂ emissions.
Typical evaluation metrics (values may vary):

R² Score: ~0.85—0.90

 MODELYEAR       MAKE                MODEL             VEHICLECLASS  \
915       2014        RAM         1500 4X4 FFV  PICKUP TRUCK - STANDARD   
316       2014      DODGE                 DART                 MID-SIZE   
886       2014    PORSCHE              BOXSTER               TWO-SEATER   
707       2014      MAZDA  MAZDA3 4-DOOR (SIL)                  COMPACT   
241       2014  CHEVROLET            SILVERADO  PICKUP TRUCK - STANDARD   

     ENGINESIZE  CYLINDERS TRANSMISSION FUELTYPE  FUELCONSUMPTION_CITY  \
915         3.6          6           A8        E                  20.5   
316         2.4          4           M6        X                  10.5   
886         2.7          6          AM7        Z                  10.7   
707         2.0          4           M6        X                   8.0   
241         6.2          8           A6        Z                  16.3   

     FUELCONSUMPTION_HWY  FUELCONSUMPTION_COMB  FUELCONSUMPTION_COMB_MPG  \
915                 14.5                  17.8                        16   
316                  6.7                   8.8                        32   
886                  7.4                   9.2                        31   
707                  5.8                   7.0                        40   
241                 11.4                  14.1                        20   

CO2EMISSIONS  
915           285  
316           202  
886           212  
...
FUELCONSUMPTION_COMB        0
FUELCONSUMPTION_COMB_MPG    0
CO2EMISSIONS                0
dtype: int64

X (Engine Size): [2.  2.4 1.5 ... 3.  3.2 3.2]
y (CO2 Emissions): [196 221 136 ... 271 260 294]
Coefficients:  38.992978724434074
Intercept:  126.28970217408721
Mean absolute error: 24.10
Mean squared error: 985.94
Root mean squared error: 31.40
R2-score: 0.76

<img width="561" height="435" alt="image" src="https://github.com/user-attachments/assets/0f71cb82-4e5f-4fa1-ab05-f70dafc36504" />
<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/75dff048-69a3-4265-ade0-265ce710f881" />
<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/c51b3109-f7eb-4894-9d9a-ad5b96658b52" />
<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/21f256f6-bc6c-4eef-ba45-b75b7be6f817" />
<img width="571" height="432" alt="image" src="https://github.com/user-attachments/assets/514cf2d2-0f5d-47eb-a1f7-4e63860482ca" />






