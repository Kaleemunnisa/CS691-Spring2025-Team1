import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import numpy as np
def predict_tennis_results(data_path, player_name, future_data):
    """
    Predicts tennis match results for a given player using RandomForestClassifier.

    Args:
        data_path (str): Path to the CSV file containing tennis match data.
        player_name (str): Name of the player for whom to make predictions.
        future_data (pd.DataFrame): DataFrame containing future match data.

    Returns:
        pd.Series: Predicted results (0 for loss, 1 for win).
    """

    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: File not found at {data_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the data: {e}")
        return None

    # Preprocessing
    data = data.dropna(subset=['Score']) # Remove rows with missing scores.
    data = data.dropna(subset=['against']) # Remove rows where opponent is unknown.
    data = data.dropna(subset=['Rk']) # Remove rows where player ranking is unknown.
    data = data.dropna(subset=['vRk']) # Remove rows where opponent ranking is unknown.
    data = data.dropna(subset=['Surface']) # Remove rows where surface is unknown.
    data = data.dropna(subset=['Aces']) # Remove rows where aces are unknown.
    data = data.dropna(subset=['DFs']) # Remove rows where double faults are unknown.
    data = data.dropna(subset=['SP']) # Remove rows where serve points are unknown.
    data = data.dropna(subset=['1SP']) # Remove rows where first serve points are unknown.
    data = data.dropna(subset=['2SP']) # Remove rows where second serve points are unknown.
    data = data.dropna(subset=['vA']) # Remove rows where opponent aces are unknown.
    data = data.dropna(subset=['Time_minutes']) # Remove rows where time is unknown.

    # Feature Engineering
    data['Result'] = data.apply(lambda row: 1 if player_name in row['Score'] and 'W' in row['Score'] or player_name == row['against'] and 'L' not in row['Score'] else 0, axis=1) # Create result column, 1 for win, 0 for loss.
    data['RankDiff'] = data['Rk'] - data['vRk'] # Ranking difference.
    data['PlayerAcesRatio'] = data['Aces'] / data['SP']
    data['OpponentAcesRatio'] = data['vA'] / data['SP']
    data['DoubleFaultRatio'] = data['DFs'] / data['SP']
    data['FirstServePercentage'] = data['1SP'] / data['SP']
    data['SecondServePercentage'] = data['2SP'] / data['SP']

    # Select relevant features
    features = ['RankDiff', 'Surface', 'PlayerAcesRatio', 'OpponentAcesRatio', 'DoubleFaultRatio', 'FirstServePercentage', 'SecondServePercentage', 'Time_minutes']

    # Encode categorical features
    label_encoders = {}
    for feature in ['Surface']:
        label_encoders[feature] = LabelEncoder()
        data[feature] = label_encoders[feature].fit_transform(data[feature])
        if feature in future_data.columns:
          future_data[feature] = label_encoders[feature].transform(future_data[feature])

    # Prepare data for training
    X = data[features]
    y = data['Result']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

    # Prepare future data
    if future_data is not None and not future_data.empty:
      future_data['RankDiff'] = future_data['Rk'] - future_data['vRk']
      future_data['PlayerAcesRatio'] = future_data['Aces'] / future_data['SP']
      future_data['OpponentAcesRatio'] = future_data['vA'] / future_data['SP']
      future_data['DoubleFaultRatio'] = future_data['DFs'] / future_data['SP']
      future_data['FirstServePercentage'] = future_data['1SP'] / future_data['SP']
      future_data['SecondServePercentage'] = future_data['2SP'] / future_data['SP']
      future_X = future_data[features]
      predictions = pd.Series(model.predict(future_X))
      return predictions
    else:
      return pd.Series()

