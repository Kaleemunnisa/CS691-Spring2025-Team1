import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import numpy as np


input_csv_file = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\raw_kaggle.csv"  # Replace with your input CSV file path
time_column = "Time"  # Replace with the name of your time column
output_csv_file_cleaned = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\output_csv_file_cleaned.csv" #Replace with your desired output file name
output_csv_file_name = output_csv_file_cleaned = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\output_csv_file_name.csv" #Replace with your desired output file name
output_csv_file_time_conv = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\output_csv_file_time_conv.csv" #Replace with your desired output file name


import filter_name
filter_name.filter_rows_by_names(input_csv_file, output_csv_file_name, ["Novak Djokovic", "Rafael Nadal"])

#data pre processsing
import data_clean
data_clean.delete_rows_with_missing_data(output_csv_file_name, output_csv_file_cleaned)


#Convert time format from HH:MM to minutes
import time_conversion
time_conversion.convert_excel_time_column_to_minutes(output_csv_file_cleaned, time_column, output_csv_file_time_conv)


data_path = output_csv_file_time_conv
player_name = 'Novak Djokovic' 


# Example future data (replace with your actual data)
future_data = pd.DataFrame({
    'Surface': ['Hard', 'Hard'],
    'Rk': [1, 1],
    'vRk': [5, 10],
    'Aces': [10, 8],
    'DFs': [2, 3],
    'SP': [80, 75],
    '1SP': [60, 55],
    '2SP': [15, 12],
    'vA': [6, 4],
    'Time_minutes': [120, 150]
})


import prediction_model

predictions = prediction_model.predict_tennis_results(data_path, player_name, future_data)

if predictions is not None and not predictions.empty:
    print("Predicted Results (1=Win, 0=Loss):")
    print(predictions)

