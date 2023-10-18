#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[3]:


df = pd.read_csv("C:\\Users\\bharath kumar\\Downloads\\mail_data.csv")


# In[4]:


print(df)


# In[5]:


data =df.where((pd.notnull(df)),'')


# In[6]:


data.head(10)


# In[7]:


data.info()


# In[8]:


data.shape


# In[ ]:





# In[34]:


# Assuming your DataFrame is named 'data'
data.loc[data['Category'] == 'spam', 'Category'] = 0
data.loc[data['Category'] == 'ham', 'Category'] = 1



# In[35]:


X = data['Message']
Y = data['Category']


# In[36]:


print(X)


# In[37]:


print(Y)


# In[38]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 3)


# In[39]:


print(X.shape)
print(X_train.shape)
print(X_test.shape)


# In[40]:


print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)


# In[41]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[42]:


# Create a TfidfVectorizer instance with specified parameters
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

# Transform the training and test data using the TfidfVectorizer
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# Convert target labels to integer type
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')


# In[43]:


print(X_train)


# In[44]:


print(X_train_features)


# In[45]:


print(Y_train)


# In[46]:


model = LogisticRegression()
model.fit(X_train_features,Y_train)


# In[ ]:





# In[47]:


prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)


# In[48]:


print('Acc on training data: ',accuracy_on_training_data)


# In[49]:


prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)


# In[ ]:





# In[50]:


print('Acc on training data: ',accuracy_on_test_data)
input_data_features = feature_extraction.transform(input_your_mail)

prediction = model.predict(input_data_features)


# In[53]:


# Assuming you have defined 'feature_extraction' and 'model' properly
input_your_mail = ["The guy did some bitching "]
input_data_features = feature_extraction.transform(input_your_mail)

prediction = model.predict(input_data_features)

print(prediction)

if (prediction[0] == 1):
    print('Ham mail')
else:
    print('Spam mail')


# In[ ]:




