# me
# 9dfd6139-159a-11e8-9de3-00505601122b

import argparse

import numpy as np
import sklearn.datasets
import sklearn.model_selection

def main(args):
    # Load Boston housing dataset
    dataset = sklearn.datasets.load_boston()
    # print(dataset.DESCR)

    # The input data are in dataset.data, targets are in dataset.target.
    data = dataset.data
    targets = dataset.target

    # TODO: Pad a value of "1" to the input data.
    data = np.pad(data, [(0,0),(0,1)], 'constant', constant_values=1)

    # TODO: Split data so that the last `args.test_size` data are the test
    # set and the rest is the training set
    d_train , d_test = data[:-args.test_size], data[-args.test_size:]
    t_train , t_test = targets[:-args.test_size], targets[-args.test_size:]

    # TODO: Solve the linear regression using the algorithm from the lecture,
    # explicitly computing the matrix inverse (using np.linalg.inv).
    trainT = d_train.T
    inverze = np.linalg.inv(trainT@d_train)
    something = inverze@trainT
    w = something@t_train

    # TODO: Predict target values on the test set
    pred_vector = [x.T@w for x in d_test]

    # TODO: Compute root mean square error on the test set predictions
    rmse = np.sqrt(np.square(pred_vector - t_test).mean())

    with open("linear_regression_manual.out", "w") as output_file:
        print("{:.2f}".format(rmse), file=output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_size", default=50, type=int, help="Test size to use")
    args = parser.parse_args()
    main(args)