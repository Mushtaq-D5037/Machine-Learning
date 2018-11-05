#### Multiple Linear Regression
predict the outcome of dependent variable based on two or more independent variables

* Y = b0 + b1X1 + b2X2 + ... + bnXn

* Y   -- Dependent variable
* X1,X2,...Xn  -- Independent Variable
* b1,b2,.. bn  -- co-efficients
* b0  -- constant / intercept

#### Assumptions of Multiple Linear Regression :

1.**Linearity** -
The relatonships between the predictors and outcome variables should be linear.
If the relationship is not linear the appropriate transformation such as log,square root and higher order polynomials ect shold
be applied to the dependent/ independent variable to fix the issue
* Linearity can be tested using **Scatter plots**

2.**Homoscedasticity and Normality** -
The error variance (the errors between observed and predicted values i.e., the residuals of the regression) should be Constant,
which is known as homoschedasticity and the error should be normally distributed

* This assumption may be checked by looking at a **histogram or a Q-Q-Plot**.
  Normality can also be checked with a **goodness of fit test** (e.g., the Kolmogorov-Smirnov test), though this test must be conducted on the residuals themselves

3.**Lack of Multicolinearity** : Independent variables should not be highly correlated to each other
* Multicollinearity may be checked multiple ways:
   * **Correlation matrix** – When computing a matrix of Pearson’s bivariate correlations among all independent variables, 
     the magnitude of the correlation coefficients should be less than .80
   * **Variance Inflation Factor (VIF)** – The VIFs of the linear regression indicate the degree that the variances in the regression estimates 
     are increased due to multicollinearity. VIF values higher than 10 indicate that multicollinearity is a problem
#### Dummy Variable Trap:
* It is a scenario in which the independent variables are multicollinear with each other ( two or more variables are highly correlated)
  in simple terms one variable can be predicted from the others
* solution is to simply drop one of the encoded categorical variable.
* one may think that on dropping one of the variable the model behaves  biased  but it won't
 in the absence of the dropped categorical variable the constant behaves as catogorical variable
#### Hypothesis:
* **Hypothesis**         - something strong assumption  regarding the distribution of the observations
* **Hypothesis testing** - Validating  hypothesis (our strong assumption) is called as hypothesis testing\

**steps**
1. hypothesis is made
2. validity of the hypothesis is tested
3. if the hypothesis is found to be true ,it is accepted ( null hypothesis)
4. if it is found to be untrue,it is rejected 
-  the hypothesis that is being tested for possible rejection is called **null hypothesis** (null hypothesis assumes that our assumption regarding the observation is true)
- the hypothesis that is accepted when null hypothesis is rejected is called **alternative hypothesis**

**level of significance/confidence**\
**p-value < 0.05** --  **reject** the null hypothesis (i.e., accept the alternative hypothesis)\
**p-value > 0.05**  -- **fail to reject** the null hypothesis (i.e., accept the null hypothesis)

**Null-Hypothesis(H0)**         - Assuming that our Hypothesis (assumption made regarding observation) is true\
**Alternative Hypothesis(H1)**  - rejecting the Null Hypothesis (proving that our assumption is not true)

**What is p-value?**\
p-value is the probability of getting **"Sample like Ours"** if the null hypothesis is true\
So, we assume the null hypothesis is true and then determine how **“strange”** our sample really is.\
If it is not that strange (a large p-value) then we don’t change our mind about the null hypothesis.\ 
As the p-value gets smaller, we start wondering if the null really is true and well maybe we should change our minds (and reject the null hypothesis).

#### Buildng a Model
5 methods of building a model
1. **all in**
2. **Backward Elimination**
3. **Forward Elimination**
4. **Bidirectional Elimination**
5. **Score Comparison**

1.**All - in :** use all variables\
when we have prior knowledge

2.**Backward Elimination**\
a) select the significance level ( say eg: sl = 0.05 or 5%)\
b) fit the model with all possible predictors\
c) consider the predictor with the highest p-value.if the p-value > significance leve go to step 4 otherwise FIN(finish the model(model is ready)\
d) Remove the predictor with the highest p-value\
e) fit the model without this variable\

3.**Forward Elimination**\
a) select a significance level to enter the model(sl=0.05)\
b) create all possible simple linear regression models ( model with one variable)\
   Fit all simple regression models (y ~ x(n)).Select the one with lowest p-value\
c) Create all posible models with one extra variable added to the previous model\ 
   Fit all possible models\
d)consider the predictor with the lowest p-value.If p<sl, go to step 3 ,otherwise go to FIN ( keep the previous model)\

4.**Bidirectional Elimination**\
a) select a significance level to ENTER and STAY in the model\
   eg:slEnter = 0.05 , slStay=0.05\
b) perform the next step of forward selection ( new variable must have p-value < slEnter)\
c) perform all steps of backwad Elimination ( old variable must have p-value<slStay)\
d) Repeat until no new variable can enter and no old variables stay\

5.**Score comparison (all possible models)**\
a) select a criterion of goodness of fit\
b) construct all possible Regression Models 2powerN - 1 total combinations\
c).select the one with the best criterion\
