import os
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), 'old_faithful.txt')
xs = np.loadtxt(path)

print(xs.shape)
print(xs[0])

plt.scatter(xs[:, 0], xs[:, 1])
plt.xlabel('Eruptions(Min)') # 噴出した時間
plt.ylabel('Waiting(Min)') # 噴出の間隔
plt.show()
