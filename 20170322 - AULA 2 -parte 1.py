#TAREFAS AULA 2 
# Implementar gerador de números aleatórios, com distribuição normal
# - Usar transformada de Box Muller
# - Gerar sequência de N=100, 1000 e 10.000 amostras
# - Plotar Histograma e comparar com PDF esperada
# - Plotar CDF obtida e comparar com CDF esperada
# - Usar sementes fixas diferentes e plotar gráficos 

from numpy import random, sqrt, log, sin, cos, pi
from pylab import show, hist, subplot, figure
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats
import pylab
import numpy
from numpy.random import rand, seed

# BOX MULLER - TRANSFORMATION FUNCTION
def gaussian(u1,u2):
  z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
  z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
  return z1,z2

# uniformly distributed values between 0 and 1 (N=100 samples)
print("Seed=10")
seed(10)
u1 = random.rand(100)
u2 = random.rand(100)
print ("variáveis aleatórias com distribuição uniforme, e N=100 amostras")
print ("u1:" , u1)
print ("u2:" , u2)

# run the transformation (N=100 samples)
z1,z2 = gaussian(u1,u2)
print ("Gaussiana - OK")
print ("variáveis aleatórias com distribuição normal, e N=100 amostras")
print ("z1:" , z1)
print ("z2:" , z2)
print("Transformation Box Muller - OK")

# plotting the values before and after the transformation
print ("HISTOGRAMAS - antes e depois da Transf. Box Muller") 
print ("1a linha => u1 e u2 -> Var. aleatorias dist. Linear")
print ("2a linha => z1 e z1 -> Var. aleatorias dist. Normal")
figure()
subplot(221) # the first row of graphs
hist(u1)     # contains the histograms of u1 and u2 
subplot(222)
hist(u2)
subplot(223) # the second contains
hist(z1)     # the histograms of z1 and z2
subplot(224)
hist(z2)
show()

# calculate and plot CDF from Z1 and Z2 (N=100 samples)
print ("Calculo e plot da CDF de z1 e z2")
num_bins_plot_cdf_z1 = 20
counts, bin_edges_z1 = np.histogram(z1, bins=num_bins_plot_cdf_z1, normed=True)
cdf_z1 = np.cumsum(counts)
pylab.plot(bin_edges_z1[1:], cdf_z1)

num_bins_plot_cdf_z2 = 20
counts, bin_edges_z2 = np.histogram(z2, bins=num_bins_plot_cdf_z2, normed=True)
cdf_z2 = np.cumsum(counts)
pylab.plot(bin_edges_z2[1:], cdf_z2)

######################################################################
# uniformly distributed values between 0 and 1 (N=100 samples)
print("seed=10")
seed(10)
u1 = random.rand(1000)
u2 = random.rand(1000)

# run the transformation
z1,z2 = gaussian(u1,u2)

# plotting the values before and after the transformation
figure()
subplot(221) # the first row of graphs
hist(u1)     # contains the histograms of u1 and u2 
subplot(222)
hist(u2)
subplot(223) # the second contains
hist(z1)     # the histograms of z1 and z2
subplot(224)
hist(z2)
show()

# uniformly distributed values between 0 and 1, 100 amostras.
print("Seed=10")
seed (10)
u1 = random.rand(10000)
u2 = random.rand(10000)

# run the transformation
z1,z2 = gaussian(u1,u2)

# plotting the values before and after the transformation
figure()
subplot(221) # the first row of graphs
hist(u1)     # contains the histograms of u1 and u2 
subplot(222)
hist(u2)
subplot(223) # the second contains
hist(z1)     # the histograms of z1 and z2
subplot(224)
hist(z2)
show()
