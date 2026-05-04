import numpy as np
import pandas as pd
import seaborn as sns
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load Dataset
df = sns.load_dataset('penguins')
df = df.dropna()

# Feature & Target
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

# Train_TEST
X_train,x_test,y_train,y_test =train_test_split(X,y,random_state=11,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

# Save Model
pickle.dump(model,open("model.pkl",'wb'))
print("Model Saved Successfully!")