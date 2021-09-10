import numpy as np
from scipy.special import  gamma
import matplotlib.pyplot as plt

theta = np.arange(0.17,0.43, 0.01)
exp_ratio = gamma(theta+2)**2 / (gamma(theta+1) * gamma(3+theta))
gauss_ratio = gamma((theta+2)/2)**2 / (gamma((theta+1)/2) * gamma((3+theta)/2))

plt.plot(theta, exp_ratio)
plt.plot(theta, gauss_ratio)

plt.xlabel("$\\theta$")
plt.ylabel(r'$\langle f \rangle^2 / \langle f^2 \rangle$')
plt.ylim([0, 1])
plt.savefig("../theory_mfr.pdf",bbox_inches="tight")
