import pandas as pd
import numpy as np

dataset = pd.read_csv('50_Startups.csv')
dataset.shape
dataset.head()

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4]

# Encoding Categorical data(State column) to Numeric
# if the categorical data is binary LabelEncoder enough
# before one hot encoding on categorical column , label Encoder must be applied

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le = LabelEncoder()
X[:,3] = le.fit_transform(X[:,3])
oneHotEncode = OneHotEncoder(categorical_features = [3])
X = oneHotEncode.fit_transform(X).toarray()

# Avoid Dummy Trap
X = X[:,1:]

# splitting data into Training and Testing set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split ( X,y,test_size = 0.2,random_state = 42)

# Fitting Multiple Linear Regression Model to training data
from sklearn.linear_model import LinearRegression
multiple_lr = LinearRegression()
multiple_lr.fit(X_train,y_train)

# predicting on Test set
y_pred = multiple_lr.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm

# equation --> Y = b0(X0) + b1X1 + b2X2 + b3X3 + b4X4
# adding X0 feature (i.e constant/intercept where x0 = 1) with 50rows 1 columns manually to the X features Matrix
# since we need to add the column to the starting of matrix we use a trick i.e,
# rather than adding ones to the matrix we add matrix to the ones so that ones comes first and matrix comes after ones
# How it should be (like below)
# X = np.append(arr = X , values = np.ones((50,1).astype(int)),axis = 1)

# taking np.ones in 'arr parameter' and X feature matrix in 'values parameter'
X = np.append(arr = np.ones((50,1)).astype(int) , values = X,axis = 1)

"""
# Backward Elimination
X_opt = X[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = y,exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,1,3,4,5]]
regressor_ols = sm.OLS(endog = y,exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,3,4,5]]
regressor_ols = sm.OLS(endog = y,exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,3,5]]
regressor_ols = sm.OLS(endog = y,exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,3]]
regressor_ols = sm.OLS(endog = y,exog = X_opt).fit()
regressor_ols.summary()
"""

# defining Backward Elimination Function
def BackwardElimination (x,sl):
    numVars = len(x[0])
    for i in range(0,numVars):
        regressor_ols = sm.OLS(y,x).fit()
        maxVar = max(regressor_ols.pvalues)
        if (maxVar > sl):
            for j in range (0,numVars - 1):
                if(regressor_ols.pvalues[j]==maxVar):
                    x = np.delete(x,j,1)
    regressor_ols.summary()
    return x

sl = 0.05
X_modeled = BackwardElimination(X_opt,sl)
