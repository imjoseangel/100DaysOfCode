#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

#Read the data
df = pd.read_csv(WORK_DIR + "/news.csv")

#Get shape and head
print("\nShape\n=====\n")
print(df.shape)
print("\nHead\n====\n")
print(df.head())

#DataFlair - Get the labels
labels = df.label
print("\nLabels\n======\n")
print(labels.head())

#DataFlair - Split the dataset
x_train, x_test, y_train, y_test = train_test_split(df['text'],
                                                    labels,
                                                    test_size=0.2,
                                                    random_state=7)

#DataFlair - Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
#DataFlair - Fit and transform train set, transform test set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

#DataFlair - Initialize a PassiveAggressiveClassifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)
#DataFlair - Predict on the test set and calculate accuracy
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score*100,2)}%')

#DataFlair - Build confusion matrix
print(confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL']))
