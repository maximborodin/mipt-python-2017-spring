import math

π = 0.0
for i in range(1, 11):
    π += pow(-1, i - 1) * 4 / (2 * i - 1)
print(π)
