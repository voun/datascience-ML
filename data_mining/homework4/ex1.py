'''
Skeleton for Homework 4: Logistic Regression and Decision Trees
Part 1: Logistic Regression

Authors: Anja Gumpinger, Dean Bodenham, Bastian Rieck
'''

#!/usr/bin/env python3

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler



def compute_metrics(y_true, y_pred):
    '''
    Computes several quality metrics of the predicted labels and prints
    them to `stdout`.

    :param y_true: true class labels
    :param y_pred: predicted class labels
    '''

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    print('Exercise 1.a')
    print('------------')
    print('TP: {0:d}'.format(tp))
    print('FP: {0:d}'.format(fp))
    print('TN: {0:d}'.format(tn))
    print('FN: {0:d}'.format(fn))
    print('Accuracy: {0:.3f}'.format(accuracy_score(y_true, y_pred)))


if __name__ == "__main__":

    ###################################################################
    train = pd.read_csv("data/diabetes_train.csv")
    test = pd.read_csv("data/diabetes_test.csv")
    scaler = StandardScaler()

    X_train = train.iloc[:,0:7].values
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(test.iloc[:,0:7].values)
    y_train = train.iloc[:,7].values
    y_test = test.iloc[:,7].values

    
    classifier = LogisticRegression()
    classifier.fit(X_train,y_train)
    y_pred = classifier.predict(X_test)
    compute_metrics(y_test,y_pred)

    ###################################################################

    print('Exercise 1.b')
    print('------------')
    print("Since we classify whether or not a person has diabetes, it is important to have" +
     " few false-negatives. Since the false-negatives are lower for LDA, I would choose LDA.")

    print('Exercise 1.c')
    print('------------')
    print("It is hard to say which one is better in general: LDA or logistic regression. "+
            "A big disadvantage with LDA is that you have to calculate the inverse of the covariance matrix, "+
             "which is very expensive in comparison to the training step in logistic regression."+
              "For this reason, I would choose logistic regression")

    print('Exercise 1.d')
    print('------------')
    print("The coefficients are:")
    print(classifier.coef_)
    print("")
    print("The interpretation of the weights is that they show how much the corresponding feature contribute "+
     "to the probability of a person having diabetes. It seems as if \"glu\" and \"ped\" affects the probability of a person having diabetes the most.")
    print("The coefficient for the npreg variable is about 0.33")
    print("Calculating the exponential function we get that the increase in odds for the npreg variable is approx 1.39.")
    print("the std for the npreg variable is " + "{0:.2f}".format(scaler.scale_[0]) + " which means that an increase in 1 pregnancy " +
            "corresponds to increasing the npreg variable in our logistic function with 1/std. " +
            "Hence, if w is the coefficient in front of the npreg variable, the risk increase exp(w/std) which is 1.10. "+
            "So the risk increase is about 10%.")



   


