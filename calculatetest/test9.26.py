from calculate import *
import matplotlib.pyplot as plt
import matplotlib

x=np.arange(0,10**(0.5),10**(0.5)/200)
test=F(x,0.5)

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(9,9))
plt.plot(x,test,linewidth=1,color='r')
plt.ylabel(r'$S_{Spherical \ crown}-S_{plane}$',fontsize='17')
plt.xlabel('Spherical Radius',fontsize='17')
plt.title('Radius in plane $r_{0}=1$',fontsize='18')
t=(r'$S_{plane}=\pi r_{0}^2 \\ S_{Spherical \ crown=2\pi R^2(1-cos\frac{r_0}{R})}$')
plt.text(1.0,0.5,'$S_{plane}=\pi r_0^2 $',fontsize='14',ha='left',wrap=True)
plt.text(1.0,0.4,'$S_{Spherical \ crown}=2\pi R^2(1-cos(r_0/R)) $',fontsize='14',ha='left',wrap=True)
plt.savefig('/users/dingding 1/desktop/homework9.26.eps')
# plt.show()

