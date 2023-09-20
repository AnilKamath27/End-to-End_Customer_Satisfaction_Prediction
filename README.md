**Project Title**: Invistico_Airline Customer Satisfaction Analysis

## Software and Tools Requirements

1. [GitHub](https://github.com/)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitHubDesktop](https://desktop.github.com/)
4. [Heroku](https://heroku.com/)


Create new enviroment

```
conda create -p venv python==3.8.17 -y
```

**Summary**:
This project is focused on analyzing customer satisfaction data for Invistico_Airline. The main goal is to gain insights into customer feedback and preferences in order to improve overall satisfaction. The project involves data preprocessing and the training of machine learning models to predict customer satisfaction levels.

This data given by an airline organization. The actual name of the company is not given due to various purposes that's why the name Invistico airlines.
The dataset consists of the details of customers who have already flown with them. The feedback of the customers on various context and their flight data has been consolidated.
The main purpose of this dataset is to predict whether a future customer would be satisfied with their service given the details of the other parameters values.
Also the airlines need to know on which aspect of the services offered by them have to be emphasized more to generate more satisfied customers.

- Gender: categorical, Female or Male
- Customer Type: categorical, Loyal Customer or disloyal Customer
- Age: Numerical, the reviewed customer’s age.
- Type of Travel: Categorical, Business travel or Personal Travel
- Class: categorical, Business, Eco, or Other
- Flight Distance: numerical, the distance for the flight being reviewed.
- Departure Delay in Minutes: numerical
- Arrival Delay in Minutes: numerical

The next 14 variables are all customer’s satisfaction level to a certain aspect of the flight. They are all numerical variables on a 0–5 scale.
- Seat comfort
- Departure/Arrival time convenient
- Food and drink
- Gate location
- Inflight wifi service
- Inflight entertainment
- Online support
- Ease of Online booking
- On-board service
- Leg room service
- Baggage handling
- Checkin service
- Cleanliness
- Online boarding

For more information visit: https://harshalvaza.medium.com/invistico-airlines-understanding-customer-satisfaction-6108b500e592

**Description**:
- **Data Preprocessing and Visualization**: The code begins by importing necessary libraries for data manipulation, visualization, model selection, preprocessing, feature selection, and evaluation. It also sets up configurations for XGBoost and TensorFlow. The dataset (`Invistico_Airline.csv`) is loaded and examined for missing values. Missing values are dropped as they are a small portion of the dataset. Data visualization is performed to understand data distributions and relationships, including visualizing the target variable 'satisfaction.'

- **Data Preprocessing**: The dataset is split into features (X) and the target variable (y). Label encoding is applied to the target variable. A ColumnTransformer is used to handle categorical and numeric features, and MinMax scaling is applied to normalize the data.

- **XGBoost Classifier**: An XGBoostClassifier is created and included in a pipeline that includes data preprocessing and feature selection using SelectKBest with the chi-squared metric. The pipeline is trained on the data, and evaluation metrics such as accuracy, ROC-AUC, precision, recall, and F1-score are calculated. A confusion matrix and ROC curve are also visualized.

- **Cross-Validation**: Cross-validation is performed to assess model performance using accuracy scores.

- **Hyperparameter Tuning**: A grid search is conducted to fine-tune the XGBoostClassifier with different hyperparameters, but it didn't significantly improve accuracy.

- **Model Serialization**: The final trained XGBoost model is serialized using the pickle library and saved as 'XGBoost_Model.pkl.'

- **Feed Forward Neural Network (FNN)**: A simple Feed Forward Neural Network (FNN) is created using TensorFlow/Keras. The FNN consists of multiple layers with different activation functions. The model is trained and evaluated, and performance metrics, including accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix, and precision-recall curve, are calculated and visualized.

- **Model Saving**: The trained FNN model is saved as 'Simple FNN.'

**Conclusion**:
This project showcases an end-to-end analysis of customer satisfaction data for Invistico_Airline. It explores both machine learning (XGBoost) and deep learning (FNN) approaches for predicting customer satisfaction. The code demonstrates data preprocessing, model training, evaluation, and serialization, providing insights and tools for improving customer satisfaction in the airline industry.