## AI-Powered Housing Price Prediction with GST/HST Compliance Check

An end-to-end MLOps pipeline leveraging Snowflake, Scikit-learn, and Streamlit to predict Canadian housing prices and assess GST/HST applicability. The project also explores conceptual AGI capabilities to enhance legal compliance, automation, and user interpretability in future implementations.

## Project Goal

To build a robust, interpretable, and deployable ML pipeline that predicts house prices based on structured housing data and flags regulatory tax compliance (GST/HST) when price exceeds $1,000,000 CAD. This project simulates how AGI could automate tax policy reasoning, user explanation, and model evolution in real time.

## Intended Audience
  # Data Scientists and ML Engineers

  # MLOps Practitioners

  # Canadian Tax Regulators and Policy Analysts

  # AI and AGI Researchers

  # Government IT/Cloud Architects

  # Real Estate Data Analysts

## Pipeline Strategy

1. Data Ingestion:
Load the Kaggle housing dataset (train.csv) into a Snowflake table named HOUSE_PRICES_RAW using snowflake-connector-python.

2. Data Preprocessing:
Use Snowflake Snowpark to clean and filter key columns (SalePrice, GrLivArea, LotArea, OverallQual) and store the result in HOUSE_PRICES_CLEAN.

3. Export Clean Data:
Convert Snowpark DataFrame to Pandas and save locally as cleaned_house_prices.csv.

4. Model Training:
Use Scikit-learn's RandomForestRegressor to train a model on selected features. Save the trained model to model.joblib.

5. Streamlit App:

Build an interactive web app that:

- Accepts user input (GrLivArea, LotArea, OverallQual)

- Predicts house price

- Flags GST/HST tax based on threshold

## Kaggle Submission:
Generate a submission.csv with predicted SalePrice for test.csv entries. An additional version submission_with_tax_flag.csv includes the GST/HST logic for demonstration.

## AGI Conceptual Extensions:
Outline how an AGI could autonomously maintain tax rules, explain predictions, and continuously improve the pipeline.

Input/Output Examples
Example 1:
Input: GrLivArea = 1500, LotArea = 5000, OverallQual = 7
Output: Estimated Price = $875,000 → ✅ No GST/HST

Example 2:
Input: GrLivArea = 2800, LotArea = 10000, OverallQual = 10
Output: Estimated Price = $1,250,000 → 🔴 GST/HST May Apply

##  Repository Structure

.
├── app.py                            # Streamlit web interface
├── cleaned_house_prices.csv         # Cleaned export from Snowflake
├── data/
│   ├── train.csv                    # Kaggle dataset
│   ├── test.csv
│   └── data_description.txt
├── notebooks/
│   └── preprocess_and_train.ipynb   # Full pipeline notebook
├── models/
│   └── model.joblib                 # Trained scikit-learn model
├── submissions/
│   ├── submission.csv
│   └── submission_with_tax_flag.csv
├── README.md
├── requirements.txt
└── LICENSE

## Conceptual AGI Extensions

This project includes a conceptual design of how an AGI-enhanced system could:

- Monitor and update GST/HST logic based on federal tax law changes.

- Provide natural language justifications for predictions (e.g., “High-quality build + large lot area”).

- Continuously retrain using new real estate data and legal precedents.

- Explain pricing rationale interactively to users and regulators.

## Quickstart
Install dependencies and run the Streamlit app

pip install -r requirements.txt
streamlit run app.py

## Requirements
1. Python 3.9+
2. Scikit-learn
3. Snowflake Connector
4. Snowpark for Python
5. Pandas, NumPy
6. Streamlit
7. joblib

## requirements.txt
pandas
numpy
scikit-learn
streamlit
snowflake-connector-python
snowflake-snowpark-python
joblib

## License
MIT License
© 2025 Ronald Kalani

## Contributing
Pull requests welcome. Please ensure any new contributions support legal interpretability and remain aligned with Canadian tax frameworks.

## Contact
Ronald Kalani
📧 ronaldkalani@yahoo.ca
🔗 LinkedIn Profile

