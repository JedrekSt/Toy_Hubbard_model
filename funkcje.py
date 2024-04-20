import numpy as np

class operators:
    sz=np.array([[1,0],[0,-1]],dtype=complex)
    Id=np.array([[1,0],[0,1]],dtype=complex)
    spl=np.array([[0,0],[1,0]],dtype=complex)

    @staticmethod
    def generate(N,m):
        cp=operators.spl
        for _ in range(0,m-1):
            cp=np.kron(operators.sz,cp)
        for _ in range(m+1,N+1):
            cp=np.kron(cp,operators.Id)
        return {'cr':cp,'an':np.transpose(np.conj(cp))}
    
    @staticmethod
    def anti_com(A,B):
        return np.dot(A,B)+np.dot(B,A)

class Hamiltonian:
    N=4
    def __init__(self):
        self.c=[operators.generate(self.N,i) for i in range(1,(self.N)+1)]
        self.cup=[self.c[item] for item in range(0,len(self.c)) if item%2==0]
        self.cdw=[self.c[item] for item in range(0,len(self.c)) if item%2!=0]
        self.sc=[{
            'x' : np.dot(self.cup[i]['cr'],self.cdw[i]['an'])+np.dot(self.cdw[i]['cr'],self.cup[i]['an']),
            'y' : -1j*(np.dot(self.cup[i]['cr'],self.cdw[i]['an'])-np.dot(self.cdw[i]['cr'],self.cup[i]['an'])),
            'z' : np.dot(self.cup[i]['cr'],self.cup[i]['an'])-np.dot(self.cdw[i]['cr'],self.cdw[i]['an'])
            }
            for i in range(len(self.cup))]
        self.S={
            'x' : sum(el['x'] for el in self.sc),
            'y' : sum(el['y'] for el in self.sc),
            'z' : sum(el['z'] for el in self.sc)
        }

    def generate_H(self,eps1,eps2,U,t,B,J):
        H_kinetic1=eps1*sum(np.dot(self.c[i]['cr'],self.c[i]['an']) for i in range(0,2))
        H_kinetic2=eps2*sum(np.dot(self.c[i]['cr'],self.c[i]['an']) for i in range(2,len(self.c)))
        H_int1=U*(np.dot(np.dot(np.dot(self.c[0]['cr'],self.c[0]['an']),self.c[1]['cr']),self.c[1]['an']))
        H_int2=U*(np.dot(np.dot(np.dot(self.c[2]['cr'],self.c[2]['an']),self.c[3]['cr']),self.c[3]['an']))
        H_hop=t*(np.dot(self.c[0]['cr'],self.c[2]['an'])+np.dot(self.c[1]['cr'],self.c[3]['an']))
        H_hop+=np.transpose(np.conj(H_hop))
        H_spin=self.S['x']*B[0]+self.S['y']*B[1]+self.S['z']*B[2]
        H_ferro=-J*(np.dot(self.S['x'],self.S['x'])+np.dot(self.S['y'],self.S['y'])+np.dot(self.S['z'],self.S['z']))
        return H_kinetic1+H_kinetic2+H_int1+H_int2+H_hop+H_spin+H_ferro

Ham=Hamiltonian()
eps1=1
eps2=2
U=1
t=0.1
B=[0,0,0.01]
J=0
H0=Ham.generate_H(eps1,eps2,U,t,B,J)
print(H0)




        

    






