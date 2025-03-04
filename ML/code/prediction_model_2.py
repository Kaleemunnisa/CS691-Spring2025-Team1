import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, accuracy_score

import time_conversion

time_conversion.convert_excel_time_column_to_minutes(r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\against_filtered.csv", 
                                                     "Time", r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\against_filtered.csv")



def predict_tennis_match_extended(player_name, opponent_name, round_val, player_rank, opponent_rank, tournament, surface):
    """
    Predicts the result and other statistics of a tennis match based on historical data.

    Args:
        player_name (str): The name of the player.
        opponent_name (str): The name of the opponent.
        round_val (str): The round of the tournament.
        player_rank (int): The player's rank.
        opponent_rank (int): The opponent's rank.
        tournament (str): The tournament name.
        surface (str): The surface of the court.

    Returns:
        dict: A dictionary containing the predicted result and statistics.
    """

    try:
        df = pd.read_csv(r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\against_filtered.csv")
    except FileNotFoundError:
        return {"error": "tennis_data.csv not found. Please provide the correct file path."}

    df = df.dropna(subset=['Score'])
    df = df.dropna(subset=['Name', 'Against_name', 'Rd', 'Rk', 'vRk', 'Tournament', 'Surface'])

    df['Result'] = df.apply(lambda row: 1 if row['Name'] in row['Score'] else 0, axis=1)

    label_encoders = {}
    categorical_cols = ['Name', 'Against_name', 'Rd', 'Tournament', 'Surface']
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    features = ['Name', 'Against_name', 'Rd', 'Rk', 'vRk', 'Tournament', 'Surface']
    target_numerical = ['TP', 'Aces', 'DFs', 'SP', '1SP', '2SP', 'vA', 'Time_minutes']
    target_classification = ['Result']

    numerical_cols = ['Rk', 'vRk']
    imputer = SimpleImputer(strategy='mean')
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    X = df[features]
    X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

    models_reg = {}
    for target in target_numerical:
        y = df[target]
        y_train, y_test = train_test_split(y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        models_reg[target] = model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"MSE for {target}: {mse}")

    model_class = RandomForestClassifier(random_state=42)
    y_class = df['Result']
    y_train_class, y_test_class = train_test_split(y_class, test_size=0.2, random_state=42)
    model_class.fit(X_train, y_train_class)
    y_pred_class = model_class.predict(X_test)
    accuracy = accuracy_score(y_test_class, y_pred_class)
    print(f"Accuracy for Result: {accuracy}")

    try:
        input_data = pd.DataFrame({
            'Name': [label_encoders['Name'].transform([player_name])[0]],
            'Against_name': [label_encoders['Against_name'].transform([opponent_name])[0]],
            'Rd': [label_encoders['Rd'].transform([round_val])[0]],
            'Rk': [player_rank],
            'vRk': [opponent_rank],
            'Tournament': [label_encoders['Tournament'].transform([tournament])[0]],
            'Surface': [label_encoders['Surface'].transform([surface])[0]]
        })
    except ValueError as e:
        if "y contains previously unseen labels" in str(e):
            return {"error": "One or more of the provided player, opponent, tournament, round, or surface values were not found in the training data."}
        else:
            return {"error": str(e)}

    input_data[numerical_cols] = imputer.transform(input_data[numerical_cols])
    input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])

    predictions_reg = {}
    for target, model in models_reg.items():
        predictions_reg[target] = model.predict(input_data)[0]

    prediction_class = model_class.predict(input_data)[0]
    result = "Win" if prediction_class == 1 else "Loss"

    predictions_reg['Result'] = result

    return {
        "prediction": predictions_reg,
        "player": player_name,
        "opponent": opponent_name,
        "round": round_val,
        "tournament": tournament,
        "surface": surface,
        "player_rank": player_rank,
        "opponent_rank": opponent_rank,
    }

player_name = "Novak Djokovic"
opponent_name = "CarlosAlcaraz"
round_val = "F"
player_rank = 1
opponent_rank = 2
tournament = "Wimbledon"
surface = "Grass"
import output_to_note

for i in range(20):
    for j in range(20):
        prediction_result = predict_tennis_match_extended(player_name, opponent_name, round_val, player_rank + i , opponent_rank + j, tournament, surface)
        print(prediction_result)
        output_to_note.append_to_note_file(prediction_result, r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\code\outputs\output.txt")


