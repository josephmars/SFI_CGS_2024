# training.py
# Trains and saves Random Forest and SVM models for the Reddit dataset

import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report

def train_models():
    # Load the preprocessed data
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/preprocessed_data.pkl', 'rb') as f:
        X, y = pickle.load(f)

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the models
    # Random Forest
    rf_classifier = OneVsRestClassifier(RandomForestClassifier(n_estimators=100, random_state=42))

    # Support Vector Machine
    svm_classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True, random_state=42))

    # Train Random Forest
    print("Training Random Forest model...")
    rf_classifier.fit(X_train, y_train)
    # Save the trained Random Forest model
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/random_forest_model.pkl', 'wb') as f:
        pickle.dump(rf_classifier, f)

    # Evaluate Random Forest
    y_pred_rf = rf_classifier.predict(X_val)
    print("Random Forest Classification Report:")
    print(classification_report(y_val, y_pred_rf, target_names=['C1 Work', 'C2 Worker', 'C3 Workforce']))

    # Train SVM
    print("Training SVM model...")
    svm_classifier.fit(X_train, y_train)
    # Save the trained SVM model
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/svm_model.pkl', 'wb') as f:
        pickle.dump(svm_classifier, f)

    # Evaluate SVM
    y_pred_svm = svm_classifier.predict(X_val)
    print("SVM Classification Report:")
    print(classification_report(y_val, y_pred_svm, target_names=['C1 Work', 'C2 Worker', 'C3 Workforce']))

    print("Models trained and saved successfully.")

if __name__ == '__main__':
    train_models()
