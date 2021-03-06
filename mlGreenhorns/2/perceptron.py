#!/usr/bin/env python3
import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--examples", default=50, type=int, help="Number of examples")
    parser.add_argument("--plot", default=False, action="store_true", help="Plot progress")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    # Generate a binary classification data with labels [-1, 1]
    data, target = sklearn.datasets.make_classification(
        n_samples=args.examples, n_features=2, n_informative=2, n_redundant=0,
        n_clusters_per_class=1, flip_y=0, class_sep=2, random_state=args.seed)
    target = 2 * target - 1

    # TODO: Append a constant feature with value 1 to the end of every input data
    data = np.pad(data, [(0,0),(0,1)], 'constant', constant_values=1)

    # Generate initial perceptron weights
    weights = np.random.uniform(size=data.shape[1])

    done = False
    while not done:
        if args.plot:
            plt.scatter(data[:, 0], data[:, 1], c=target)
            xs = np.linspace(*plt.gca().get_xbound() + (20,))
            ys = np.linspace(*plt.gca().get_ybound() + (20,))
            plt.contour(xs, ys, [[[x, y, 1] @ weights for x in xs] for y in ys], levels=[0])
            plt.show()

        # TODO: Implement the perceptron algorithm, notably one iteration
        # over the training data in sequential order. (In practise we might
        # consider also processing the examples in a randomized order.)
        # For incorrectly examples perform the required update to the `weights`.
        # If all training instances are correctly separated, set `done=True`,
        # otherwise set `done=False`.
        done = True
        for i in range(len(data)):
            y_i = weights.T @ data[i]
            if target[i] * y_i < 0:
                weights += target[i]*data[i]
                done = False


    print(" ".join("{:.2f}".format(weight) for weight in weights))