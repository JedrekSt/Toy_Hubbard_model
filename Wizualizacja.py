from funkcje import *
from matplotlib import pyplot as plt
import numpy as np
import scipy

#Stworzenie klasy służącej do generowania Hamiltonianów
Ham=Hamiltonian(4) 

#definiiowanie parametrów układu
U,t,B,J=1,0.1,[0,0,0.1],0
Tem=0.01
eps1=np.arange(-1.5,1.5,0.025)
eps2=np.arange(-1.5,1.5,0.025)

#operatory, których średnia będzie liczona
n=Ham.particle_num()
skw=Ham.squared_s()
s1s2=Ham.conjunction()
sz=Ham.spin_z()

#rezerwacja pamięci dla macierzy wizualizowanych
ans_n=np.zeros((len(eps1),len(eps2)))
ans_skw=ans_n.copy()
ans_s1s2=ans_n.copy()
ans_sz=ans_n.copy()


for ep1 in range(len(eps1)):
    for ep2 in range(len(eps2)):
        H = Ham.generate_H(eps1[ep1],eps2[ep2],U,t,B,J)
        rho = scipy.linalg.expm(-H/Tem)
        rho = rho/np.trace(rho)
        ans_n[ep1,ep2] = np.trace(np.dot(n,rho))
        ans_skw[ep1,ep2] = np.trace(np.dot(skw,rho))
        ans_s1s2[ep1,ep2] = np.trace(np.dot(s1s2,rho))
        ans_sz[ep1,ep2] = np.trace(np.dot(sz,rho))

fig,ax=plt.subplots(2,2)
fig.subplots_adjust(hspace=0.5, wspace=0.5)
Ans=[[ans_n,ans_skw],[ans_s1s2,ans_sz]]
Ans_title=[[r'$\langle n\rangle$',r'$\langle S^{2}\rangle$'],[r'$\langle \vec{S}_{1}\cdot \vec{S}_{2}\rangle$',r'$\langle S_{z}\rangle$']]

for i in range(2):
    for j in range(2):
        img=ax[i,j].imshow(Ans[i][j],extent=(eps1[0],eps1[-1],eps2[0],eps2[-1]),cmap='plasma')
        ax[i,j].set_title(Ans_title[i][j])
        ax[i,j].set_xlabel(r'$\varepsilon_{1}/U$')
        ax[i,j].set_ylabel(r'$\varepsilon_{2}/U$')
        fig.colorbar(img, ax=ax[i,j])

plt.show()



