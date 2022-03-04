import numpy as np
data = list(range(20, 100, 5))
print(data)

Q1 = np.quantile(data, 0.25)
Q2 = np.quantile(data, 0.50)
Q3 = np.quantile(data, 0.75)

print("Quartile 1 : ", Q1)
print("Quartile 2 : ", Q2)
print("Quartile 3 : ", Q3)

def QuartileDeviation(a, b):
    return (a - b)/2
print(QuartileDeviation(Q3, Q1))
