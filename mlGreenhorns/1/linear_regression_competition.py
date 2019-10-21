#!/usr/bin/env python3
# cooperated with
# 3619d41d-b80b-11e7-a937-00505601122b


import argparse
import pickle
import numpy as np
import matplotlib.pyplot as plt


from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import Lars
from sklearn.linear_model import LassoLars
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import TheilSenRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import ExtraTreesRegressor


parser = argparse.ArgumentParser()
parser.add_argument("--model_path", default="linear_regression_competition.model", type=str, help="Model path")
parser.add_argument("--seed", default=42, type=int, help="Random seed")

def pick_algorithm():
    # Choose the right model
    pipelines = []
    pipelines.append(('ScaledLR', Pipeline([('Scaler', StandardScaler()),('LR',LinearRegression())])))
    pipelines.append(('ScaledSGDR', Pipeline([('Scaler', StandardScaler()),('SGDR',SGDRegressor())])))
    pipelines.append(('ScaledHR', Pipeline([('Scaler', StandardScaler()),('HR',HuberRegressor())])))
    pipelines.append(('ScaledLARS', Pipeline([('Scaler', StandardScaler()),('LARS',Lars())])))
    pipelines.append(('ScaledLL', Pipeline([('Scaler', StandardScaler()),('LL',LassoLars())])))
    pipelines.append(('ScaledORP', Pipeline([('Scaler', StandardScaler()),('ORP',OrthogonalMatchingPursuit())])))
    pipelines.append(('ScaledPAR', Pipeline([('Scaler', StandardScaler()),('PAR',PassiveAggressiveRegressor())])))
    pipelines.append(('ScaledBR', Pipeline([('Scaler', StandardScaler()),('BR',BayesianRidge())])))
    pipelines.append(('ScaledRIDGE', Pipeline([('Scaler', StandardScaler()),('RIDGE', Ridge())])))
    pipelines.append(('ScaledLASSO', Pipeline([('Scaler', StandardScaler()),('LASSO', Lasso())])))
    pipelines.append(('ScaledEN', Pipeline([('Scaler', StandardScaler()),('EN', ElasticNet())])))
    pipelines.append(('ScaledKNN', Pipeline([('Scaler', StandardScaler()),('KNN', KNeighborsRegressor())])))
    pipelines.append(('ScaledCART', Pipeline([('Scaler', StandardScaler()),('CART', DecisionTreeRegressor())])))
    pipelines.append(('ScaledGBM', Pipeline([('Scaler', StandardScaler()),('GBM', GradientBoostingRegressor())])))
    pipelines.append(('ScaledABR', Pipeline([('Scaler', StandardScaler()),('ABR', AdaBoostRegressor())])))
    pipelines.append(('ScaledBAR', Pipeline([('Scaler', StandardScaler()),('BAR', BaggingRegressor())])))

    results = []
    names = []
    for name, model in pipelines:
        kfold = KFold(n_splits=10, random_state=args.seed)
        cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring='neg_mean_squared_error')
        results.append(cv_results)
        names.append(name)
        msg = f"{name}: {cv_results.mean()}"
        print(msg)

def twist_params(model):
    # Choose the right estimator
    scaler = StandardScaler().fit(x_train)
    rescaledX = scaler.transform(x_train)
    param_grid = dict(n_estimators=np.arange(400,601,100))

    kfold = KFold(n_splits=10, random_state=args.seed)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring='neg_mean_squared_error', cv=kfold)
    #grid = GridSearchCV(estimator=model, scoring='neg_mean_squared_error', cv=kfold)
    grid_result = grid.fit(rescaledX, y_train)

    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print(f"{mean} with estimator: {param}")

    print(f"Best: {grid_result.best_score_} using {grid_result.best_params_}")

def train_model(model):
    # Train the model
    scaler = StandardScaler().fit(x_train)
    rescaled_xtrain = scaler.transform(x_train)
    model.fit(rescaled_xtrain, y_train)
    return model, scaler


def recodex_predict(data):
    # The `data` is a Numpy array containt test set input.

    args = parser.parse_args([])

    with open(args.model_path, "rb") as model_file:
        model = pickle.load(model_file)

    scaler = StandardScaler().fit(data)
    rescaled_data = scaler.transform(data)
    # TODO: Return the predictions as a Numpy array.
    return model.predict(rescaled_data)


if __name__ == "__main__":
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Load the data to train["data"] and train["target"]
    train = np.load("linear_regression_competition.train.npz")
    x_train, x, y_train, y = train_test_split(train["data"], \
            train["target"], test_size=.1, random_state=args.seed)

    model = BaggingRegressor(random_state=args.seed, n_estimators=500)
    #pick_algorithm(model)

    #twist_params(model)

    model, scaler = train_model(model)

    # Validate the model
    rescaled_x = scaler.transform(x)
    pred = model.predict(rescaled_x)
    pred = recodex_predict(x)
    print (np.sqrt(mean_squared_error(y, pred)))

    with open(args.model_path, "wb") as model_file:
        pickle.dump(model, model_file)
