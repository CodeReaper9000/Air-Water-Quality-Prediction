# Air-Water-Quality-Prediction
## Problem Statement

Considering the importance of air and water to human existence, air pollution
and water pollution are critical issues that require collective effort for prevention
and control. Different types of anthropogenic activities have resulted in
environmental dilapidation and ruin. One of the tools that can be used for such
a campaign is Air Quality Index (AQI). The AQI was based on the concentrations
of different pollutants: We are also familiar with the Water Quality Index (WQI),
which in simple terms tells what the quality of drinking water is from a drinking
water supply. There is a need for constant and continuous environment
monitoring of air quality and water quality for the development of AQI and WQI,
which in turn will enable clear communication of how clean or unhealthy the air
and water in the stud area is.

## Data Collection
1) https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india
2) https://www.kaggle.com/datasets/anbarivan/indian-water-quality-data

## Model Selected
### Random Forest
I employed a Random Forest model for AQI prediction after comparing it with Linear Regression and Support Vector Regressor. The Random Forest model demonstrated superior performance, achieving a lower Mean Squared Error and providing more accurate results.

## Technologies Used
1) Python: For data processing, machine learning, and model development.
2) Pandas & NumPy: For data manipulation and numerical operations.
3) Matplotlib & Seaborn: For visualizing data and relationships between pollutants and AQI. 
4) Scikit-learn: For implementing machine learning models (Random Forest, Linear Regression, SVR) and hyperparameter tuning.
5) Joblib: For saving and loading the trained machine learning model.
6) HTML/CSS: For designing the frontend to allow user input and display predictions.
7) Flask: To create a web application and serve the machine learning model for predictions.
