# -*- coding: utf-8 -*-
"""Network Anomaly Detection(genetic algorithm) complete.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15SPam9bFETRNw8VIXtAPN5cRFfyqVM2x

**Applying Genetic Algorithm**
"""

# Install DEAP for genetic algorithms
!pip install deap

import pandas as pd
import numpy as np
from deap import base, creator, tools, algorithms
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Google Colab drive mounting
from google.colab import drive
drive.mount('/content/drive')

# Load the data
file_path = '/content/drive/MyDrive/Network_Anomaly_Detection/ACI-IoT.xlsx'
data = pd.read_excel(file_path)

# Handle infinite values
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Encoding categorical features
categorical_features = data.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()
for col in categorical_features:
    data[col] = label_encoder.fit_transform(data[col])

# Handle missing values
imputer = SimpleImputer(strategy='mean')
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Separate features and targets
X = data.drop('Label', axis=1)
y = data['Label'].astype(int)

# Print column names to check the exact name of the 'Label' column
df = pd.read_excel(file_path)
print(df.columns)

# Define evaluation function first
def eval_features(individual):
    features = [X.columns[index] for index in range(len(individual)) if individual[index] == 1]
    if len(features) == 0:
        return 0,  # Handling empty feature subset

    X_train, X_test, y_train, y_test = train_test_split(X[features], y, test_size=0.3, random_state=42)
    clf = RandomForestClassifier(n_estimators=10)  # Reduced from 100
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy,

from deap import base, creator, tools

# DEAP setup for genetic algorithm

if not hasattr(creator, "FitnessMax"):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # Maximizing fitness function

if not hasattr(creator, "Individual"):
    creator.create("Individual", list, fitness=creator.FitnessMax)

# Setup the toolbox
toolbox = base.Toolbox()
toolbox.register("attr_bool", np.random.randint, 0, 2)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(X.columns))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eval_features)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Initialize population and run the genetic algorithm
population = toolbox.population(n=30)
ngen = 20  # Number of generations
result, log = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=ngen, verbose=True)

# Print the best individual found
best_ind = tools.selBest(population, 1)[0]
print("Best individual is: %s\nwith fitness: %s" % (best_ind, best_ind.fitness.values))

"""**Applying Machine Learning**"""

# Assuming 'best_ind' contains the best individual from the GA output
selected_features = [X.columns[i] for i in range(len(best_ind)) if best_ind[i] == 1]
X_selected = X[selected_features]

from sklearn.model_selection import train_test_split

# Split the data - using 70% for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.3, random_state=42)

from sklearn.ensemble import RandomForestClassifier

# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

"""**Graphs**"""

#Feature Importance Visualization

import matplotlib.pyplot as plt

feature_importances = model.feature_importances_
indices = np.argsort(feature_importances)[::-1]

# Rearrange feature names so they match the sorted feature importances
names = [X_selected.columns[i] for i in indices]

plt.figure(figsize=(15, 5))
plt.title("Feature Importances")
plt.bar(range(X_selected.shape[1]), feature_importances[indices])
plt.xticks(range(X_selected.shape[1]), names, rotation=90)
plt.show()

#Confusion Matrix Heatmap

import seaborn as sns

# Convert confusion matrix to DataFrame for easier plotting
conf_matrix_df = pd.DataFrame(confusion_matrix(y_test, y_pred), index=model.classes_, columns=model.classes_)

plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix_df, annot=True, fmt="d", cmap="Blues")
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

#Accuracy Over Generations

# Assuming 'log' is the DEAP logbook from the genetic algorithm
gen = log.select("gen")
fit_max = log.select("max")

plt.figure(figsize=(10, 5))
plt.plot(gen, fit_max, label='Max Fitness')
plt.xlabel('Generation')
plt.ylabel('Max Fitness')
plt.title('Max Fitness per Generation')
plt.legend()
plt.show()

#ROC Curve for Each Class

from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

# Binarize the output classes
y_bin = label_binarize(y, classes=np.unique(y))
n_classes = y_bin.shape[1]

# Split the data - using the original data before feature selection for full ROC analysis
X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X, y_bin, test_size=0.3, random_state=42)

# Learn to predict each class against the other using the RandomForestClassifier
classifier = OneVsRestClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
classifier.fit(X_train_full, y_train_full)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test_full[:, i], classifier.predict_proba(X_test_full)[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plotting
plt.figure(figsize=(10, 8))
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f'Class {i} (area = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic for Each Class')
plt.legend(loc="lower right")
plt.show()

