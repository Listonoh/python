#!/usr/bin/env python3
# cooperated with
# 3619d41d-b80b-11e7-a937-00505601122b

import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

def accuracy(weights, X, Y):
    acc = sum([np.argmax(weights.T @ X[i]) == Y[i] for i in range(X.shape[0])])
    return acc / X.shape[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_size", default=10, type=int, help="Batch size")
    parser.add_argument("--classes", default=10, type=int, help="Number of classes to use")
    parser.add_argument("--iterations", default=50, type=int, help="Number of iterations over the data")
    parser.add_argument("--learning_rate", default=0.01, type=float, help="Learning rate")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--test_size", default=797, type=int, help="Test set size")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Use the digits dataset
    data, target = sklearn.datasets.load_digits(n_class=args.classes, return_X_y=True)

    # Append a constant feature with value 1 to the end of every input data
    data = np.pad(data, ((0, 0), (0, 1)), constant_values=1)

    # Split the data randomly to train and test using `sklearn.model_selection.train_test_split`,
    # with `test_size=args.test_size` and `random_state=args.seed`.
    train_data, test_data, train_target, test_target = sklearn.model_selection.train_test_split(
        data, target, stratify=target, test_size=args.test_size, random_state=args.seed)

    # Generate initial model weights
    weights = np.random.uniform(size=[train_data.shape[1], args.classes])

    for iteration in range(args.iterations):
        permutation = np.random.permutation(train_data.shape[0])

        # TODO: Process the data in the order of `permutation`.
        # For every `args.batch_size`, average their gradient, and update the weights.
        # You can assume that `args.batch_size` exactly divides `train_data.shape[0]`.
        batches = np.array_split(permutation, len(permutation)/ args.batch_size)

        for batch in batches:
            X, Y = train_data[batch], train_target[batch]
            grd = np.zeros(shape=weights.T.shape)
            for i in range(X.shape[0]):
                e = np.exp((X[i] @ weights) - np.max(X[i] @ weights))
                sm = e / e.sum(axis=0)
                sm[Y[i]] -= 1
                grd += np.outer(sm, X[i])
            grd /= args.batch_size
            weights -= args.learning_rate * grd.T

        # TODO: After the SGD iteration, measure the accuracy for both the
        # train test and the test set and print it in percentages.

        train_accuracy, test_accuracy =\
            accuracy(weights, train_data, train_target), accuracy(weights, test_data, test_target)
        print("After iteration {}: train acc {:.1f}%, test acc {:.1f}%".format(
            iteration + 1,
            100 * train_accuracy,
            100 * test_accuracy,
        ))
