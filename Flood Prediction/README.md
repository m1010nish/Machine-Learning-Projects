# Flood Prediction Using Machine Learning

📊 Climate Classifier Comparison 🌐

Overview

This repository contains a Python script for comparing multiple machine learning classifiers on a climate dataset. The dataset, loaded from Google Drive, includes monthly weather features. The script utilizes popular classifiers such as K-Nearest Neighbors, Logistic Regression, Decision Tree, Support Vector, and Random Forest for predicting the occurrence of floods.
📈 Metrics

The classifiers are evaluated based on key metrics:

    Accuracy: The overall correctness of predictions.
    Precision: The accuracy of positive predictions.
    Recall: The ability to capture all positive instances.
    F1 Score: The balance between precision and recall.

🧠 Machine Learning Models

    K-Nearest Neighbors (KNN): Grid search is used to optimize the number of neighbors.
    Logistic Regression: Hyperparameter tuning performed using grid search.
    Decision Tree: Grid search for optimal criterion and maximum depth.
    Support Vector Classifier (SVC): Tuning for C value and kernel type.
    Random Forest: Classification with a specified maximum depth.

📊 Visualization

    Heatmap: Correlation matrix visualized using Seaborn.
    Histograms: Distribution of specific weather features.

🤖 Model Evaluation

Metrics for each classifier are displayed in a tabular format using Plotly. It provides a quick comparison of the models' performance.
🚀 Usage

    Mount Google Drive to access the dataset.
    Preprocess the data, replace labels, and visualize correlations.
    Split the data into training and testing sets (90% training, 10% testing).
    Normalize features using MinMaxScaler.
    Train classifiers: KNN, Logistic Regression, Decision Tree, Support Vector, Random Forest.
    Evaluate and compare performance metrics.
    Generate an interactive table for easy metric comparison.

🌟 Conclusion

Explore the README for a detailed overview of the climate classification models and their respective performances.

Feel free to fork, contribute, and enhance the project! 🌍🌤️🔍
