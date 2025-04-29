import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# === Step 1: Load Dataset ===
df = pd.read_csv(r"/Users/ushareddy/Desktop/ml/CS691-Spring2025-Team1-ML-prediction/ML/datasets/against_filtered.csv")

# === Step 2: Define win/loss extraction for ANY player ===
def extract_label(row):
    score = row['Score']
    sets = re.findall(r'(\d+)\(?(\d*)\)?-(\d+)\(?(\d*)\)?', score)
    
    if sets:
        player_sets = [int(set[0]) for set in sets]
        opponent_sets = [int(set[2]) for set in sets]
        player_wins = sum(1 for ps, os in zip(player_sets, opponent_sets) if ps > os)
        return 1 if player_wins > len(sets) / 2 else 0
    else:
        return np.nan

df['label'] = df.apply(extract_label, axis=1)
df.dropna(subset=['label'], inplace=True)

# === Step 3: Set features and target ===
X = df.drop(columns=['label'])
y = df['label']

# === Step 4: Identify categorical and numerical columns ===
categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

# === Step 5: Preprocessing ===
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)],
    remainder='passthrough'
)

# === Step 6: Create Pipeline with Gradient Boosting ===
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GradientBoostingClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    ))
])

# === Step 7: Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 8: Train the Model ===
model.fit(X_train, y_train)

# === Step 9: Predict and Evaluate ===
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# === Step 10: Confusion Matrix ===
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Loss', 'Win'], yticklabels=['Loss', 'Win'])
plt.title("Confusion Matrix")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()

# === Step 11: Accuracy and Loss Bar Plots ===
# Accuracy
plt.figure(figsize=(6, 4))
sns.barplot(x=["Gradient Boosting"], y=[accuracy], palette='viridis')
plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# Loss
plt.figure(figsize=(6, 4))
sns.barplot(x=["Gradient Boosting"], y=[1 - accuracy], palette='magma')
plt.title("Model Misclassification (Loss)")
plt.ylabel("Loss (1 - Accuracy)")
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
