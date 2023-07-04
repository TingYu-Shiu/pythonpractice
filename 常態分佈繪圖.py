import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 16.0

mean = 8.0 
std = 2.0

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std) #完美常態分布

plt.plot(x,y, color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.25)

plt.title('How to plot a normal distribution in python with matplotlib',fontsize=10)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
plt.show()


#---------------------------

mean = 100
std = 15
low = 115
high = np.inf
# x = 40-100-160
x_min = 40
x_max = 160
# y = normal distribution
x = np.linspace(x_min, x_max, 100)
y = scipy.stats.norm.pdf(x,mean,std)
plt.plot(x,y, color='coral')
plt.grid()
plt.xlim(x_min,x_max)
plt.ylim(0,0.05)
# 標籤們
plt.title('Normal Distribution of IQ scores',fontsize=10)
plt.xlabel('IQ')
plt.ylabel('Probability')

#print (1 - scipy.stats.norm.pdf(low ,mean, std))
# fill area between x = low x = high

pt1 = low
plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')

pt2 = x_max
plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')

ptx = np.linspace(pt1, pt2, 10)
pty = scipy.stats.norm.pdf(ptx,mean,std)

plt.fill_between(ptx, pty, color='#0b559f', alpha=1.0)
area = 1 - scipy.stats.norm.cdf(low, mean, std)
#cdf累積機率(1-到115前的面積)