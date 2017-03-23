import numpy as np
import matplotlib.pyplot as plt
import pylab

#calculate and plot PDF
print ("Calculo e plot da PDF")
x=10
A=1
h = plt.hist(np.random.triangular(0, A*x, 10, 10000000), bins=200, normed=True)
plt.show()

#calculate and plot CDF
print ("Calculo e plot da CDF")
x1=A*x
num_bins_plot_cdf_x1 = 20
counts, bin_edges_x1 = np.histogram(x1, bins=num_bins_plot_cdf_x1, normed=True)
cdf_x1 = np.cumsum(counts)
pylab.plot(bin_edges_x1[1:], cdf_x1)
