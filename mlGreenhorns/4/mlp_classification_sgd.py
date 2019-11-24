#!/usr/bin/env python3
import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

def dReLU(x):
    return [1 if i > 0 else 0 for i in x]

def accuracy(X, y):
    acc = sum([np.argmax(forward(X[i])[1]) == y[i] for i in range(X.shape[0])])
    return acc / X.shape[0]

def gradient(w, X, y):
    grad = [np.zeros_like(w[0]), np.zeros_like(w[1])]
    for i in range(X.shape[0]):
        h, sm = forward(X[i])
        sm[y[i]] -= 1
        dh = (sm @ w[1].T) * dReLU(X[i] @ w[0])

        grad[0] += np.outer(X[i], dh)
        grad[1] += np.outer(h, sm)

    grad[0], grad[1] = grad[0] / args.batch_size, grad[1] / args.batch_size
    return grad

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_size", default=10, type=int, help="Batch size")
    parser.add_argument("--classes", default=10, type=int, help="Number of classes to use")
    parser.add_argument("--hidden_layer", default=20, type=int, help="Hidden layer size")
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
    weights = [np.random.uniform(size=[train_data.shape[1], args.hidden_layer], low=-0.1, high=0.1),
               np.random.uniform(size=[args.hidden_layer, args.classes], low=-0.1, high=0.1)]

    def forward(inputs):
        # TODO: Implement forward propagation, returning *both* the value of the hidden
        # layer and the value of the output layer.
        #
        # We assume a neural network with a single hidden layer of size `args.hidden_layer`
        # and ReLU activation, where ReLU(x) = max(x, 0), and an output layer with softmax
        # activation.
        #
        # The value of the hidden layer is computed as ReLU(inputs times weights[0]).
        # The value of the output layer is computed as softmax(hidden_layer times weights[1]).
        #
        # Note that you need to be careful when computing softmax, because the exponentiation
        # in softmax can easily overflow. To avoid it, you can use the fact that
        # softmax(z) = softmax(z + any_constant) and compute softmax(z) = softmax(z - maximum_of_z).
        # That way we only exponentiate values which are non-positive, and overflow does not occur.
        h = np.maximum(0, inputs @ weights[0])
        e = np.exp((h @ weights[1]) - np.max(h @ weights[1]))
        sm = e / e.sum(axis=0)
        return h, sm


    for iteration in range(args.iterations):
        permutation = np.random.permutation(train_data.shape[0])

        # TODO: Process the data in the order of `permutation`.
        # For every `args.batch_size`, average their gradient, and update the weights.
        # You can assume that `args.batch_size` exactly divides `train_data.shape[0]`.
        #
        # The gradient used in SGD has now two parts, gradient of weghts[0] and weights[1].
        #
        # You can either compute the gradient directly from the neural network formula,
        # i.e., as a gradient of -log P(target | data), or you can compute
        # it "step by step" using chain rule of derivatives, in the following order:
        # - compute the derivative of the loss with respect to *inputs* of the
        #   softmax on the last layer (we did this already in softmax_classification_sgd)
        # - compute the derivative with respect to weights[1]
        # - compute the derivative with respect to the hidden layer output
        # - compute the derivative with respect to the hidden layer input
        # - compute the derivative with respect to weights[0]
        batches = np.array_split(permutation, len(permutation) / args.batch_size)

        for batch in batches:
            X_batch, Y_batch = train_data[batch], train_target[batch]
            grad = gradient(weights, X_batch, Y_batch)
            weights[0] -= args.learning_rate * grad[0]
            weights[1] -= args.learning_rate * grad[1]

        # TODO: After the SGD iteration, measure the accuracy for both the
        # train test and the test set and print it in percentages.
        train_acc = accuracy(train_data, train_target)
        test_acc = accuracy(test_data, test_target)
        print("After iteration {}: train acc {:.1f}%, test acc {:.1f}%".format(
            iteration + 1,
            100 * train_acc,
            100 * test_acc
        ))
