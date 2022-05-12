#Your task here is simply to try and re-create the following plot:
  #Colour index vs colour index vs redshift plot

#You use the pyplot module of matplotlib which has already been imported and is accessed through plt. In particular you use the plt.scatter() function, with additional arguments s, c and cmap.

#We are interested in the 'u-g' and 'r-i' colour indices.
#You make use of the plt.colorbar() function to show your scatter plots colour argument(c) to a colour bar on the side of the plot.
#Make sure you implement x and y labels and give your plot a title.



import numpy as np
from matplotlib import pyplot as plt

data = np.load('sdss_galaxy_colors_limz.npy')
cmap = plt.get_cmap('YlOrRd')                                  #to create a color map

ug = data['u'] - data['g']                                     #to define color index 'u-g'
ri = data['r'] - data['i']                                     #to define color index 'r-i'

redshift = data['redshift']                                    #to create a redshift array

plot = plt.scatter(ug, ri, s=0.5, lw=0, c=redshift, cmap=cmap) #to create a plot

cb = plt.colorbar(plot)
cb.set_label('Redshift')

#to define your axis labels and plot title
plt.xlabel('Colour index  u-g')
plt.ylabel('Colour index  r-i')
plt.title('Redshift (colour) u-g versus r-i')

#to set axis limits
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

plt.show()
