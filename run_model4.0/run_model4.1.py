#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:01:40 2017

@author: Iris
"""

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.linear_model import LogisticRegression
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.model_selection import KFold
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import metrics
import pickle
from sklearn.decomposition import TruncatedSVD as tsvd

sms = pd.read_csv('training_text.txt', encoding= 'UTF8', 
                    sep="\\|\\|",header=None, engine='python', 
                    names=['cli_data'])
sms2= pd.read_csv('training_variants.txt', encoding= 'UTF8', 
                    header=None,delimiter=',', engine='python', 
                    names=['gene','mutation','classification'])
X1 = sms.cli_data
y1= sms2.classification
RAD_NUM = [25]
for i in RAD_NUM:
    print("now running random_num{}".format(i))
    X = X1[pd.notnull(X1)]
    y = y1[pd.notnull(y1)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i)
    print(type(X_train))
    weighted=y_train.value_counts()
    weight_dict=dict()
    for key in weighted.keys():
        weight_dict[key]=1/ (weighted[key]/2490)
    vect = CountVectorizer(analyzer = 'word', stop_words = 'english', encoding= 'UTF8',
                           decode_error = 'ignore', ngram_range = (1, 3), min_df =0.00005)
    X_train_dtm = vect.fit_transform(X_train)
    X_test_dtm = vect.transform(X_test)
    VECT_NAME = 'vect_inst_radm{}.pickle'.format(i)
    with open(VECT_NAME, 'wb') as f:
        pickle.dump(vect, f)
    #model selecting

    TRUN_DIMS = [70]
    ACCURACY_LOG = dict()
    ACCURACY_SVC = dict()
    ACCURACY_LSVC = dict()
    for m in TRUN_DIMS:
        print("now truncating {}".format(m))
        svd = tsvd(n_components = m)
        X_train_reduced= svd.fit_transform(X_train_dtm)
        TRUN_NAME = 'trun_inst_ran{}_dims{}.pickle'.format(i, m)
        with open(TRUN_NAME, 'wb') as f:
            pickle.dump(svd, f)
        X_test_reduced = svd.transform(X_test_dtm)
        C_NUM = [ 0.5, 1, 5, 10]
        for c in C_NUM:
            TOL = [0.00001, 0.001, 0.1]
            for t in TOL:
                #for logistic regression model
                print("now running random_num{} truncating {} C_num{} tol_num{}".format(i, m, c, t))
                logreg = LogisticRegression(C = c, tol = t, class_weight=weight_dict)
                logreg.fit(X_train_reduced, y_train)
                LOG_NAME = "log_inst_ran{}_dims{}_C{}_tol{}.pickle".format(i, m, c, t)
                key_log =  "log_inst_ran{}_dims{}_C{}_tol{}".format(i, m, c, t)
                with open(LOG_NAME, 'wb') as f:
                    pickle.dump(logreg, f)
                y_pred_class_log=logreg.predict(X_test_reduced)
                accuracy_log = metrics.accuracy_score(y_test, y_pred_class_log)
                print("acurracy for log is {}".format(accuracy_log))
                ACCURACY_LOG[key_log] = accuracy_log
                #SVCmodel
                svc=SVC(C = c, tol = t, class_weight=weight_dict)   
                svc.fit(X_train_reduced,y_train)
                y_pred_class_svc = svc.predict(X_test_reduced)
                accuracy_svc = metrics.accuracy_score(y_test, y_pred_class_svc)  
                print("acurracy for svc is {}".format(accuracy_svc))
                SVC_NAME = "svc_inst_ran{}_dims{}_C{}_tol{}.pickle".format(i, m, c, t)
                key_svc = "svc_inst_ran{}_dims{}_C{}_tol{}".format(i, m, c, t)
                ACCURACY_SVC[key_svc] = accuracy_svc
                with open(SVC_NAME, 'wb') as f:
                    pickle.dump(svc, f)
                #linearSVC model
                clf = LinearSVC(C = c, tol = t, class_weight=weight_dict)
                clf.fit(X_train_reduced, y_train)
                LSVC_NAME = "lsvc_inst_ran{}_dims{}_C{}_tol{}.pickle".format(i, m, c,t)
                with open(LSVC_NAME, 'wb') as f:
                    pickle.dump(clf, f)
                key_lsvc =  "lsvc_inst_ran{}_dims{}_C{}_tol{}".format(i, m, c, t)
                y_pred_class_clf = clf.predict(X_test_reduced)
                accuracy_lsvc = metrics.accuracy_score(y_test, y_pred_class_clf)
                print("acurracy for lsvc is {}".format(accuracy_lsvc))
                ACCURACY_LSVC[key_lsvc] = accuracy_lsvc
max_reg = max(ACCURACY_LOG, key = lambda p: p[1])
value_reg = ACCURACY_LOG[max_reg]
max_svc = max(ACCURACY_SVC, key = lambda p: p[1])
value_svc = ACCURACY_SVC[max_svc]
max_lsvc = max(ACCURACY_LSVC, key = lambda p: p[1])
value_lsvc = ACCURACY_LSVC[max_lsvc]
print(ACCURACY_LOG)
print(ACCURACY_SVC)
print(ACCURACY_LSVC)
print("for logistic model the best result happens in model-{}-the accuracy is {}.".format(max_reg, value_reg))
print("for SVC model the best result happens in model-{}-the accuracy is {}.".format(max_svc, value_svc))            
print("for linear SVC model the best result happens in model-{}-the accuracy is {}.".format(max_lsvc, value_lsvc))            
