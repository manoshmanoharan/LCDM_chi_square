# Python module for Scientific plotting.
# Manosh T Manohharan
# Department of Physics and Centre for Particle Physics
# CUSAT, India. 
# Start date: 2 April, 2020.

import matplotlib.pyplot as plt
import numpy as np
# START #
def confidence_plot_label(x, y, z,xl,yl,t,fn):
    plt.style.use('classic')
    plt.style.use('seaborn-white')
    plt.figure(figsize=(6,6))
    bf = min([min(r) for r in z])
    for u in range(len(y)):
        for v in range(len(x)):
            if(z[u,v]<=min([min(r) for r in z])):
                i = u
                j = v
                break
    b1 = plt.contourf(x,y,z,levels=[bf,bf+2.3,bf+6.17,bf+11.8],cmap='Greys_r')
    b2 = plt.contour(x,y,z,levels=[bf,bf+2.3,bf+6.17,bf+11.8],
                     colors='k',linestyles='solid',linewidths=1)
    proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) for pc in b1.collections]
    label = [r"$1\sigma$", r"$2\sigma$", r"$3\sigma$"]
    plt.legend(proxy,label)
    plt.plot(x[j], y[i], marker='*', markersize=15, color="k",mfc='w')
    plt.xlim(min(x)-max(x)/25,max(x)+max(x)/25)
    plt.ylim(min(y)-max(y)/25,max(y)+max(y)/25)
    plt.minorticks_on()
    plt.tick_params(which='major',direction='in',length=7,labeltop=True,
                    labelleft=True,labelright=True,width=2,labelsize=20)
    plt.tick_params(which='minor',direction='in',length=4,width=2)
    plt.xlabel(xl,fontsize=20,fontweight='bold')
    plt.ylabel(yl,fontsize=20,fontweight='bold')
    plt.title(t,fontsize=15,fontweight='bold',loc='right',y=1.08,alpha=0.5)
    plt.savefig(fn,bbox_inches = 'tight')
# END #