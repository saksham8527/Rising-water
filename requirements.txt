{
    "best_model_name": "XGBoost",
    "features": [
        "Annual_Rainfall",
        "Seasonal_Rainfall",
        "Cloud_Cover",
        "Humidity",
        "Temperature",
        "Visibility",
        "Pressure",
        "Wind_Speed",
        "River_Level",
        "Soil_Moisture"
    ],
    "comparison": {
        "Decision Tree": {
            "accuracy": 0.968,
            "precision": 0.9748,
            "recall": 0.9826,
            "f1_score": 0.9787,
            "confusion_matrix": [
                [
                    234,
                    19
                ],
                [
                    13,
                    734
                ]
            ],
            "classification_report": "              precision    recall  f1-score   support\n\n           0       0.95      0.92      0.94       253\n           1       0.97      0.98      0.98       747\n\n    accuracy                           0.97      1000\n   macro avg       0.96      0.95      0.96      1000\nweighted avg       0.97      0.97      0.97      1000\n"
        },
        "Random Forest": {
            "accuracy": 0.975,
            "precision": 0.9801,
            "recall": 0.9866,
            "f1_score": 0.9833,
            "confusion_matrix": [
                [
                    238,
                    15
                ],
                [
                    10,
                    737
                ]
            ],
            "classification_report": "              precision    recall  f1-score   support\n\n           0       0.96      0.94      0.95       253\n           1       0.98      0.99      0.98       747\n\n    accuracy                           0.97      1000\n   macro avg       0.97      0.96      0.97      1000\nweighted avg       0.97      0.97      0.97      1000\n"
        },
        "KNN": {
            "accuracy": 0.973,
            "precision": 0.9813,
            "recall": 0.9826,
            "f1_score": 0.9819,
            "confusion_matrix": [
                [
                    239,
                    14
                ],
                [
                    13,
                    734
                ]
            ],
            "classification_report": "              precision    recall  f1-score   support\n\n           0       0.95      0.94      0.95       253\n           1       0.98      0.98      0.98       747\n\n    accuracy                           0.97      1000\n   macro avg       0.96      0.96      0.96      1000\nweighted avg       0.97      0.97      0.97      1000\n"
        },
        "XGBoost": {
            "accuracy": 0.975,
            "precision": 0.9775,
            "recall": 0.9893,
            "f1_score": 0.9834,
            "confusion_matrix": [
                [
                    236,
                    17
                ],
                [
                    8,
                    739
                ]
            ],
            "classification_report": "              precision    recall  f1-score   support\n\n           0       0.97      0.93      0.95       253\n           1       0.98      0.99      0.98       747\n\n    accuracy                           0.97      1000\n   macro avg       0.97      0.96      0.97      1000\nweighted avg       0.97      0.97      0.97      1000\n"
        }
    }
}