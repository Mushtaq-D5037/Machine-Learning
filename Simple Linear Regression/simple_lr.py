# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# read data
data = pd.read_csv('Salary_Data.csv')
data.shape
data.head()

# splitting data into training and testing set
from sklearn.model_selection import train_test_split

X = data.drop('Salary',axis = 1)
y = data['Salary']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42)

# fitting Simple Linear Regression to Training set

# fit ( y = b + b1X )
# y  --  dependent variable
# X  --  independent variable
# b  --  constant
# b1 --  co-efficient / slope

from sklearn.linear_model import LinearRegression

simple_lr = LinearRegression()
simple_lr.fit(X_train,y_train)

# predicting the test set result
y_pred = simple_lr.predict(X_test)

# visualizing the training set results
plt.scatter(X_train,y_train,color = 'red')
plt.plot(X_train,simple_lr.predict(X_train),color = 'blue')
plt.title('Simple Linear Regression (Training Set)')
plt.xlabel('Experience')
plt.ylabel('Salary in $')
plt.show()

# visualizing the test set result
plt.scatter(X_test,y_test,color ='green')
plt.plot(X_test,y_pred,color = 'blue')
plt.title('Simple Linear Regression (Test Set)')
plt.xlabel('Experience')
plt.ylabel('Salary in $')
plt.show()
