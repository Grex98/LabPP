#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


# In[2]:


BreastCancer = pd.read_csv('C:\BreastCanceer-data.csv')
BreastCancer.head()


# In[3]:


BreastCancer.info()


# In[4]:

BreastCancer.drop(['ID'], axis=1)
BreastCancer['Diagnosis'] = pd.factorize(BreastCancer['Diagnosis'])[0]
BreastCancer.head()

BreastCancer.info()


# In[7]:


X = BreastCancer.drop(['Diagnosis'], axis=1)
Y = BreastCancer['Diagnosis']


# In[14]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 21)
mlp = MLPClassifier(hidden_layer_sizes=(64, 40))
mlp.fit(X_train, y_train)
print("Правильность на обучающем наборе: {:.2f}".format(mlp.score(X_train, y_train)))
print("Правильность в тестовом наборе: {:.2f}".format(mlp.score(X_test, y_test)))


# In[15]:


print(mlp.predict(X_test))


# In[16]:


print(y_test.values)


# In[ ]: