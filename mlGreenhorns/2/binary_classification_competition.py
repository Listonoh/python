#!/usr/bin/env python3
# cooperated with
# 3619d41d-b80b-11e7-a937-00505601122b
import argparse
import lzma
import pickle
import os
import urllib.request
import sys

import numpy as np
import pandas as pd
import sklearn.linear_model
import sklearn.ensemble
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.tree
import sklearn.feature_selection
import sklearn.compose
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
class Dataset:
    def __init__(self,
                 name="binary_classification_competition.train.csv.xz",
                 url="https://ufal.mff.cuni.cz/~straka/courses/npfl129/1920/datasets/"):
        if not os.path.exists(name):
            print("Downloading dataset {}...".format(name), file=sys.stderr)
            urllib.request.urlretrieve(url + name, filename=name)

        # Load the dataset and split it into `train_target` (column Target)
        # and `train_data` (all other columns).
        dataset = pd.read_csv(name)
        self.data, self.target = dataset.drop("Target", axis=1), dataset["Target"]

def pick_estimator(train):
    raw_data = train.data.apply(lambda x: pd.factorize(x, sort=True)[0])
    # Polynomial features
    poly = sklearn.preprocessing.PolynomialFeatures(2, include_bias=False)

    # Categorical features
    cat = [1, 3, 5, 6, 7, 8, 9, 13]
    nc = list(range(train.data.shape[1]))
    nc = list(set(nc) - set(cat))
    ct = sklearn.compose.ColumnTransformer([("Cat", sklearn.preprocessing.OneHotEncoder(), cat), ("Non-cat", sklearn.preprocessing.StandardScaler(), nc)])

    # Pipelines
    pipelines = []
    pipelines.append(("ScaledBC", Pipeline([("Poly", poly),("Scaler", ct), ("BC", BaggingClassifier())])))
    pipelines.append(("NonPolyScaledBC", Pipeline([("Scaler", ct), ("BC", BaggingClassifier())])))
    #pipelines.append(("ScaledDT", Pipeline([("Poly", poly), ("Scaler", ct), ("DT", DecisionTreeClassifier())])))
    #pipelines.append(("ScaledEDT", Pipeline([("Poly", poly), ("Scaler", ct), ("EDT", ExtraTreeClassifier())])))
    #pipelines.append(("ScaledMLP", Pipeline([("Poly", poly), ("Scaler", ct), ("MLP", MLPClassifier())])))
    res = []
    nam = []
    for name, model in pipelines:
        kfold = KFold(n_splits=10, random_state=args.seed)
        cv_results = cross_val_score(model, raw_data, train.target, cv=kfold, scoring='accuracy')
        res.append(cv_results)
        nam.append(name)
        msg = f"{name} : {cv_results.mean()}"
        print(msg)

def cross_validate():
    #raw_data = train.data.apply(lambda x: pd.factorize(x, sort=True)[0])

    cf = train.data.select_dtypes(include=['object'])
    cf = cf.apply(lambda x: pd.factorize(x, sort=True)[0])
    train.data.update(cf)
    raw_data = train.data
    print(raw_data)
    poly = sklearn.preprocessing.PolynomialFeatures(3, interaction_only=True, include_bias=False)

    # Categorical features
    cat = [1, 3, 5, 6, 7, 8, 9, 13]
    nc = list(range(train.data.shape[1]))
    nc = list(set(nc) - set(cat))
    ct = sklearn.compose.ColumnTransformer([("Non-cat", sklearn.preprocessing.StandardScaler(), nc), ("Cat", sklearn.preprocessing.OneHotEncoder(), cat)])

    pipeline = Pipeline([("ct" , ct)])
    raw_data = pipeline.fit_transform(raw_data)
    print(raw_data)
    print(raw_data.shape)
    param_grid = dict(bootstrap_features=[True], n_estimators=[200], oob_score=[False])

    model = BaggingClassifier(n_jobs=-1)
    kfold = KFold(10)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy')
    grid_result = grid.fit(raw_data, train.target)

    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print(f"{mean} wirh: {param}")

    print(f"Best: {grid_result.best_score_} using {grid_result.best_params_}")

def build_model(train):
    cf = train.data.select_dtypes(include=['object'])
    cf = cf.apply(lambda x: pd.factorize(x, sort=True)[0])
    train.data.update(cf)
    raw_data = train.data

    cat = [1, 3, 5, 6, 7, 8, 9, 13]
    nc = list(range(train.data.shape[1]))
    nc = list(set(nc) - set(cat))
    ct = sklearn.compose.ColumnTransformer([("Non-cat", sklearn.preprocessing.StandardScaler(), nc),("Cat", sklearn.preprocessing.OneHotEncoder(), cat)])

    raw_data = ct.fit_transform(raw_data)

    model = BaggingClassifier(n_estimators=200, bootstrap_features=True).fit(raw_data, train.target)
    return model

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", default="binary_classification_competition.model", type=str, help="Model path")
parser.add_argument("--seed", default=42, type=int, help="Random seed")

if __name__ == "__main__":
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Load the dataset, downloading it if required
    train = Dataset()

    # TODO: Train the model.

#    pick_estimator(train)
    #cross_validate()
    model = build_model(train)

    # TODO: The trained model needs to be saved. All sklearn models can
    # be serialized and deserialized using the standard `pickle` module.
    # Additionally, we can also compress the model.
    #
    # To save a model, open a target file for binary access, and use
    # `pickle.dump` to save the model to the opened file:
    with lzma.open(args.model_path, "wb") as model_file:
        pickle.dump(model, model_file)
