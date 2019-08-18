# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 07:44:19 2019

@author: Ini PC
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import string
import re

from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_colwidth', 100)

def load_data():
    data = pd.read_csv('Weekend Jakarta/SabtuPagi(Jakarta).csv')
    return data

tweet_df = load_data()
tweet_df.head()

print(load_data())