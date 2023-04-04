import numpy as np
import matplotlib.pyplot as plt

def divided_difference(x: np.ndarray, y: np.ndarray) -> np.ndarray:

    n = x.shape[0]
    result = np.zeros([n, n])
    # the first column is y
    result[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            result[i][j] = (result[i+1][j-1] - result[i][j-1]) / (x[j+i] - x[i])

    return result

def newton_poly(coef: np.ndarray, x_data: np.ndarray, x: np.ndarray) -> np.ndarray:

    n = x_data.shape[0] - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x - x_data[n-k])*p 
    return p

x = np.array([-5, -1, 0, 2])
y = np.array([-2, 10, 1, 3])

a_s = divided_difference(x, y)[0, :]

x_new = np.arange(-5, 2.1, 0.0001)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)