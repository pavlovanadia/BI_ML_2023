import numpy as np


def binary_classification_metrics(y_pred, y_true, beau=False):
    """
    Computes metrics for binary classification
    Arguments:
    y_pred, np array (num_samples) - model predictions
    y_true, np array (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    """

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    tp = np.sum(np.logical_and(y_pred == 1, y_true == 1))
    tn = np.sum(np.logical_and(y_pred == 0, y_true == 0))
    fp = np.sum(np.logical_and(y_pred == 1, y_true == 0))
    fn = np.sum(np.logical_and(y_pred == 0, y_true == 1))

    try:
        precision_score = tp / (tp + fp)
    except ZeroDivisionError:
        precision_score = None
        print("Precision can not be estimated as far as there are no positive-class predictions.")
    
    try:
        recall_score = tp / (tp + fn) # as far as it is binarry classification we should refer to recall as sensitivity
    except ZeroDivisionError:
        recall_score = None
        print("Recall can not be estimated as far as there are no positive-class objects in the training set.")

    try:
        f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score)
    except ZeroDivisionError:
        f1_score = None
        print("F1 can not be estimated as far as there are no true positive predictions.")

    try:
        accuracy_score = (tp + tn) / (tp + tn + fp + fn)
    except ZeroDivisionError:
        accuracy_score = None
        print("Accuracy can not be estimated as fas as the arrays are empty.")
    
    if beau:
        separ = '\n'
        print(f'Precision: {precision_score}{separ}Recall: {recall_score}{separ}F1-score: {f1_score}{separ}Accuracy: {accuracy_score}')

    return precision_score, recall_score, f1_score, accuracy_score


def multiclass_accuracy(y_pred, y_true):
    """
    Computes metrics for multiclass classification
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    """

    """
    YOUR CODE IS HERE
    """

    tp = np.sum(y_true == y_pred)
    acc = tp / len(y_true)
    
    return acc


def r_squared(y_pred, y_true):
    """
    Computes r-squared for regression
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    r2 - r-squared value
    """

    """
    YOUR CODE IS HERE
    """
    err_pred = np.sum(np.square(y_true - y_pred))
    err_true = np.sum(np.square(y_true - np.mean(y_true)))
    r_2 = 1 - err_pred / err_true
    return r_2


def mse(y_pred, y_true):
    """
    Computes mean squared error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mse - mean squared error
    """

    """
    YOUR CODE IS HERE
    """
    err_pred = np.sum(np.square(y_true - y_pred))
    mse = err_pred / y_pred.shape[0]
    return mse


def mae(y_pred, y_true):
    """
    Computes mean absolut error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mae - mean absolut error
    """

    """
    YOUR CODE IS HERE
    """
    err_pred = np.sum(np.abs(y_true - y_pred))
    mae = err_pred / y_pred.shape[0]
    return mae
    