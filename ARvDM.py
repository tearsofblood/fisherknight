# This code illustrates the comparision between autoregressive and dynamic models. More information can be found here: https://fisherknight.com/autoregressive-vs-dynamic-models/  

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate synthetic data
np.random.seed(0)
n = 100  # Number of data points
X = np.random.uniform(low=-5, high=5, size=n)
Y = np.sin(X) + np.random.normal(scale=0.2, size=n)  # True underlying relationship: Y = sin(X) + epsilon

# Run autoregressive model
ar_model = sm.tsa.AutoReg(Y, lags=1)
ar_results = ar_model.fit()

# Define dynamic model (First-order difference equation)
dynamic_model = [Y[0]]  # Initial condition
for i in range(1, n):
    dynamic_model.append(dynamic_model[i - 1] + np.sin(X[i - 1]) + np.random.normal(scale=0.2))

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, label='Observed Data')
plt.plot(X[1:], ar_results.fittedvalues, color='red', label='Autoregressive Model')
plt.plot(X[:-1], dynamic_model[:-1], color='blue', label='Dynamic Model')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparison of Autoregressive and Dynamic Models')
plt.legend()
plt.show()
