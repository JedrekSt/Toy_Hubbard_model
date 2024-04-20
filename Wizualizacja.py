from funkcje import *

Ham=Hamiltonian()
eps1=1
eps2=2
U=1
t=0.1
B=[0,0,0.01]
J=0
H0=Ham.generate_H(eps1,eps2,U,t,B,J)
print(H0)