import numpy as np
import matplotlib.pyplot as plt
import os

original_xs = np.loadtxt(os.path.join(os.path.dirname(__file__), 'old_faithful.txt'))

params = np.load(os.path.join(os.path.dirname(__file__), 'gmm_params.npy'), allow_pickle=True).item()
phis = params['phis']
mus = params['mus']
covs = params['covs']

N = 500
new_xs = np.zeros((N, 2))
for n in range(N):
    k = np.random.choice(2, p=phis)
    mu, cov = mus[k], covs[k]
    new_xs[n] = np.random.multivariate_normal(mu, cov)


plt.scatter(original_xs[:,0], original_xs[:,1], alpha=0.7, label='original')
plt.scatter(new_xs[:,0], new_xs[:,1], alpha=0.7, label='generated')
plt.legend()
plt.xlabel('Eruptions(Min)')
plt.ylabel('Waiting(Min)')
plt.show()