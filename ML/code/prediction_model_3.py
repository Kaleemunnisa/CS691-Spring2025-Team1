import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

def train_and_predict(df, player_name, opponent_name, rd, rk, vrk, tournament, surface):
    """
    Trains a machine learning model and predicts future values based on input.

    Args:
        df (pd.DataFrame): The input DataFrame.
        player_name (str): The player's name.
        opponent_name (str): The opponent's name.
        rd (str): The round.
        rk (int): The player's rank.
        vrk (int): The opponent's rank.
        tournament (str): The tournament name.
        surface (str): The surface type.

    Returns:
        dict: A dictionary containing predicted values.
    """
    # Preprocessing
    df_copy = df.copy()
    le_name = LabelEncoder()
    le_tournament = LabelEncoder()
    le_surface = LabelEncoder()
    le_rd = LabelEncoder()

    df_copy['Name'] = le_name.fit_transform(df_copy['Name'])
    df_copy['against'] = le_name.transform(df_copy['against'])
    df_copy['Tournament'] = le_tournament.fit_transform(df_copy['Tournament'])
    df_copy['Surface'] = le_surface.fit_transform(df_copy['Surface'])
    df_copy['Rd'] = le_rd.fit_transform(df_copy['Rd'])

    # Feature selection and target variables
    features = ['Name', 'against', 'Rd', 'Rk', 'vRk', 'Tournament', 'Surface']
    targets = ['Score', 'TP', 'Aces', 'DFs', 'SP', '1SP', '2SP', 'vA', 'Time']

    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    df_copy[targets] = imputer.fit_transform(df_copy[targets])

    X = df_copy[features]
    y = df_copy[targets]

    # Model training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prepare input for prediction
    input_data = pd.DataFrame({
        'Name': [le_name.transform([player_name])[0]],
        'against': [le_name.transform([opponent_name])[0]],
        'Rd': [le_rd.transform([rd])[0]],
        'Rk': [rk],
        'vRk': [vrk],
        'Tournament': [le_tournament.transform([tournament])[0]],
        'Surface': [le_surface.transform([surface])[0]]
    })

    # Prediction
    predictions = model.predict(input_data)
    predictions_dict = {
        'Score': predictions[0][0],
        'TP': predictions[0][1],
        'Aces': predictions[0][2],
        'DFs': predictions[0][3],
        'SP': predictions[0][4],
        '1SP': predictions[0][5],
        '2SP': predictions[0][6],
        'vA': predictions[0][7],
        'Time': predictions[0][8]
    }

    return predictions_dict

# Example usage (replace with your actual data)
data = {
    'Name': ['Roger Federer', 'Rafael Nadal', 'Roger Federer', 'Rafael Nadal', 'Roger Federer', 'Rafael Nadal'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Tournament': ['Australian Open', 'Australian Open', 'Wimbledon', 'Wimbledon', 'US Open', 'US Open'],
    'Surface': ['Hard', 'Hard', 'Grass', 'Grass', 'Hard', 'Hard'],
    'Rd': ['R1', 'R1', 'R2', 'R2', 'SF', 'SF'],
    'Rk': [1, 2, 1, 2, 1, 2],
    'vRk': [50, 40, 30, 20, 10, 5],
    'against': ['Novak Djokovic', 'Andy Murray', 'Andy Murray', 'Novak Djokovic', 'Andy Murray', 'Novak Djokovic'],
    'Score': ['6-4, 6-3', '7-6, 6-2', '6-3, 7-5', '6-4, 7-6', '7-6, 6-4', '6-3, 6-4'],
    'TP': [100, 110, 120, 130, 140, 150],
    'Aces': [10, 12, 15, 18, 20, 22],
    'DFs': [2, 3, 4, 5, 6, 7],
    'SP': [60, 65, 70, 75, 80, 85],
    '1SP': [80, 85, 90, 92, 95, 98],
    '2SP': [60, 65, 70, 75, 80, 85],
    'vA': [30, 35, 40, 45, 50, 55],
    'Time': [120, 130, 140, 150, 160, 170]
}

df = pd.DataFrame(data)

# Example prediction
player = 'Roger Federer'
opponent = 'Novak Djokovic'
round_val = 'F'
rank = 1
opponent_rank = 3
tournament_val = 'French Open'
surface_val = 'Clay'

predictions = train_and_predict(df, player, opponent, round_val, rank, opponent_rank, tournament_val, surface_val)
print(predictions)

#Save the model
# joblib.dump(model, 'tennis_model.joblib')
#Load the model
# loaded_model = joblib.load('tennis_model.joblib')