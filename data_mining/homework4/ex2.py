#!/usr/bin/env python3

'''
Skeleton for Homework 4: Logistic Regression and Decision Trees
Part 2: Decision Trees

Authors: Anja Gumpinger, Bastian Rieck
'''

import numpy as np
import sklearn.datasets
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score



if __name__ == '__main__':

    iris = sklearn.datasets.load_iris()
    X = iris.data
    y = iris.target

    feature_names = iris.feature_names
    num_features = len(set(feature_names))

    ####################################################################
    
    def compute_information_content(y):   

        tot = len(y)
        if tot == 0:
            return 0
        probabilities = [len((y[y == i]))/tot for i in range(0,3)]
        probabilities = list(filter(lambda x: x > 0, probabilities))

        sum = 0
        for prob in probabilities:
            sum += -prob*np.log2(prob)          
        return sum
    
    def split_data(X,y,attribute_index,theta):

        bools = np.zeros(len(X),dtype=bool)
        for index,row in enumerate(X):
            if row[attribute_index] < theta:
                bools[index] = True
            else:
                bools[index] = False            
        invertedBools = np.logical_not(bools)
        return (X[bools],y[bools],X[invertedBools],y[invertedBools])

    def compute_information_a(X,y,attribute_index,theta):

        D1_X,D1_y,D2_X,D2_y = split_data(X,y,attribute_index,theta)

        return 1/len(y)*(len(D1_y)*compute_information_content(D1_y)+
                        len(D2_y)*compute_information_content(D2_y))

    def compute_information_gain(X,y,attribute_index,theta):
        return compute_information_content(y)-compute_information_a(X,y,attribute_index,theta)

    ####################################################################

    print('Exercise 2.b')
    print('------------')

    print("Split ( sepal length (cm) < 5.5 ): information gain = "+"{0:.2f}".format(compute_information_gain(X,y,0,5.5)))                                           
    print("Split ( sepal width (cm)  < 3.0 ): information gain = "+"{0:.2f}".format(compute_information_gain(X,y,1,3.0)))                                               
    print("Split ( petal length (cm) < 2.0 ): information gain = "+"{0:.2f}".format(compute_information_gain(X,y,2,2.0)))
    print("Split ( petal width (cm)  < 1.0 ): information gain = " +"{0:.2f}".format(compute_information_gain(X,y,3,1.0)))
                                                

    print('')

    print('Exercise 2.c')
    print('------------')
    print("I would select ( petal length (cm) < 2.0 ) or ( petal width (cm)  < 1.0 ) "+
                    "in the first split because they have the highest information gain.")

    print('')

    np.random.seed(42) 
    ####################################################################
    def avg_accuracy_and_importance(X,y,folds):
        kf = KFold(n_splits = folds,shuffle=True)
        sum = 0
        importances = []
        for train_index,test_index in kf.split(X,y):
            X_train, y_train = X[train_index],y[train_index]
            X_test, y_test = X[test_index],y[test_index]
            classifier = DecisionTreeClassifier()
            classifier.fit(X_train,y_train)
            y_pred = classifier.predict(X_test)
            sum += accuracy_score(y_test,y_pred)
            importances.append(classifier.feature_importances_)
        return (sum/folds,np.array(importances))
        

    ####################################################################

    # Do _not_ remove this line because you will get different splits
    # which make your results different from the expected ones...
    np.random.seed(42) 
    avg_acc,importances = avg_accuracy_and_importance(X,y,5)

    print('Accuracy score using cross-validation')
    print('-------------------------------------\n')
    print("The mean accuracy is " + "{0:.4f}".format(avg_acc))


    print('')
    print('Feature importances for _original_ data set')
    print('-------------------------------------------\n')
    print(importances)
    print("")
    print("It seems as if the two last features (petal length and petal width)"+
                    " are the most important features")

    print('')
    print('Feature importances for _reduced_ data set')
    print('------------------------------------------\n')
    np.random.seed(42)
    X = X[y != 2]
    y = y[y != 2]
    avg_acc,importances = avg_accuracy_and_importance(X,y,5)
    print(importances)

    print("")
    print("It seems as if the two last features (petal length and petal width)"+
                    " are the most important features, and especially the second last feature.")
    print("")
    print("The feature importance measures the reduction in impurity (or chaos) when splitting "
                +" on that particular attribute/feature. By this we mean the reduction in impurity"+
                "from parent node to the two child nodes. In our data set we can see that in 4 of the 5 times"+
            " in the k-fold cross validation, splitting on the second last feature results in two total pure child nodes.")



