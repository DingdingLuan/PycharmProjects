import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import matplotlib

#transcript the formula to calculate dl:
h=0.71
H0=1/(3.09*10**17)
c=2.99792458*10**8
def dl(Z,omegal,omegam):
    integrateportion=quad(lambda x:1/np.sqrt(omegam*(1+x)**3+omegal),0,Z)
    dl=c*(1+Z)/(h*H0)*integrateportion[0]
    return dl*10**2

#plot the result with different \Omega_{\Lambda}:
Omega=np.arange(0,1.0,0.01)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
fig=plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(111)
logz=np.arange(0,1.1,0.01)
for i in range(len(Omega)):
    Dl=[]
    for j in range(len(logz)):
        Dl=np.append(Dl,dl(10**logz[j]-1,Omega[i],1-Omega[i]))
    ax1.plot(logz, np.log10(Dl), linewidth=0.6, color='r', linestyle='-')
ax1.set_xlabel(r'$\log(z+1)$')
ax1.set_xlim(10**(-2.1),1)
ax1.set_ylim(26.5,30)
ax1.set_ylabel(r'$D_{L} \quad [log(cm)$]')
plt.text(0.6,28.6,'$\Omega_{\Lambda}=0$',fontsize='12',rotation=23,ha='left',wrap=True)
plt.text(0.57,29.15,'$\Omega_{\Lambda}=1$',fontsize='12',rotation=30,ha='left',wrap=True)
# plt.text(0.5,27.5,'$D_{L}(z)=\\frac{c(1+z)}{H_0}\\int{0}{z}\\frac{dz^,}{\sqrt{\Omega_m(1+z^,)^3+\Omega_\Lambda}}$',fontsize='15',ha='left',wrap=True)
plt.title('$Homework11.1 \quad from \quad TCLuan$')
plt.savefig('/users/dingding 1/desktop/homework11.1.jpg')
plt.show()




