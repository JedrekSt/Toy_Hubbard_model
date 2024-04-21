# Analiza dwupoziomowego modelu Andersona

## Hamiltonian modelu
Hamiltonian rozważanego układu można zapisać jako:

```math
H=\sum_{\sigma=\uparrow,\downarrow}(\varepsilon_{1}c^{\dagger}_{1\sigma}c_{1\sigma}+\varepsilon_{2}c^{\dagger}_{2\sigma}c_{2\sigma})+U\sum_{n=1,2}c_{n\uparrow}^{\dagger}c_{n\uparrow}c_{n\downarrow}^{\dagger}c_{n\downarrow}+t(\sum_{\sigma=\uparrow,\downarrow}c^{\dagger}_{1\sigma}c_{2\sigma}+h.c.)-\vec{S}\cdot\vec{B}-J\vec{S}_{1}\cdot\vec{S}_{2}.
```

- $`H_{k}=\sum_{\sigma=\uparrow,\downarrow}(\varepsilon_{1}c^{\dagger}_{1\sigma}c_{1\sigma}+\varepsilon_{2}c^{\dagger}_{2\sigma}c_{2\sigma})`$ reprezentuje energię kinetyczną na obydwu poziomach sumowaną po dwóch możliwych stanach spinowych
- $`H_{U}=U\sum_{n=1,2}c_{n\uparrow}^{\dagger}c_{n\uparrow}c_{n\downarrow}^{\dagger}c_{n\downarrow}`$ jest energią oddziaływania cząstek o przeciwnym spinie na tym samym poziomie
- $`H_{t}=t(\sum_{\sigma=\uparrow,\downarrow}c^{\dagger}_{1\sigma}c_{2\sigma}+h.c.)`$ jest energią związaną z przeskokami cząstek pomiędzy poziomami bez zmiany spinu
- $`H_{S}=-\vec{S}\cdot\vec{B}`$ jest energią oddziaływania spinów z polem magnetycznym. Operator spinu zdefiniowany jest jako:
```math
\vec{S}=\sum_{n=1,2}\vec{S}_{n}  
```
```math
\vec{S}_{n}=
\frac{\hbar}{2}\left(\begin{array}{c}
c^{\dagger}_{n\downarrow}c_{n\uparrow}+c^{\dagger}_{n\uparrow}c_{n\downarrow}\\
ic^{\dagger}_{n\downarrow}c_{n\uparrow}-ic^{\dagger}_{n\uparrow}c_{n\downarrow}\\
c^{\dagger}_{n\uparrow}c_{n\uparrow}-c^{\dagger}_{n\downarrow}c_{n\downarrow} \\
\end{array}
\right)
```
- $`H_{1,2}=-J\vec{S}_{1}\cdot\vec{S}_{2}`$ jest energią oddziaływania spinów na dwóch poziomach

Powyższe fermionowe operatory kreacji i anihilacji spełniają regularne reguły antykomutacji:
```math
\{ c_{n\sigma}^{\dagger},c_{n',\sigma'}^{\dagger} \}=\{ c_{n\sigma},c_{n',\sigma'} \}=0
```
```math
\{ c_{n\sigma},c_{n',\sigma'}^{\dagger} \}=\delta_{nn'}\delta_{kk'}
```
Stan całkowicie obsadzony zdefiniowany jest przez:
```math
| 1_{\uparrow},1_{\downarrow},1_{\uparrow},1_{\downarrow}\rangle=c_{1\uparrow}^{\dagger}c_{1\downarrow}^{\dagger}c_{2\uparrow}^{\dagger}c_{2\downarrow}^{\dagger}|0_{\uparrow},0_{\downarrow},0_{\uparrow},0_{\downarrow}\rangle
```
## Symetrie Hamiltonianu

W celu znalezienia symetrii Hamiltonianu obliczamy następujące komutatory:
```math
[n,n_{n'\sigma'}]=
\sum_{\sigma,n}(c^{\dagger}_{n\sigma}c_{n\sigma}c^{\dagger}_{n'\sigma'}c_{n'\sigma'}-c^{\dagger}_{n'\sigma'}c_{n'\sigma'}c^{\dagger}_{n\sigma}c_{n\sigma})=
```
```math
=\sum_{\sigma,n}(-c^{\dagger}_{n\sigma}c^{\dagger}_{n'\sigma'}c_{n\sigma}c_{n'\sigma'}+c^{\dagger}_{n\sigma}\delta_{nn'}\delta_{\sigma\sigma'}c_{n'\sigma'}+c^{\dagger}_{n'\sigma'}c^{\dagger}_{n\sigma}c_{n'\sigma'}c_{n\sigma}-
c^{\dagger}_{n'\sigma'}\delta_{nn'}\delta_{\sigma\sigma'}c_{n\sigma})=0
```
```math
[n,c_{n\sigma}^{\dagger}c_{n+1,\sigma}]=\sum_{\sigma',n'}(c_{n'\sigma'}^{\dagger}c_{n'\sigma'}c_{n\sigma}^{\dagger}c_{n+1,\sigma}-
c_{n\sigma}^{\dagger}c_{n+1,\sigma}c_{n'\sigma'}^{\dagger}c_{n'\sigma'})=
```
```math
=\sum_{\sigma',n'}
(-c_{n'\sigma'}^{\dagger}c_{n\sigma}^{\dagger}c_{n'\sigma'}c_{n+1,\sigma}+c_{n'\sigma'}^{\dagger}\delta_{nn'}\delta_{\sigma\sigma'}c_{n+1,\sigma}
+c_{n\sigma}^{\dagger}c_{n'\sigma'}^{\dagger}c_{n+1,\sigma}c_{n'\sigma'}-c_{n\sigma}^{\dagger}\delta_{n+1,n'}\delta_{\sigma\sigma'}c_{n'\sigma'})=0
```
```math
[n,c^{\dagger}_{n\uparrow}c_{n\downarrow}]=\sum_{\sigma' n'}(c^{\dagger}_{n'\sigma'}c_{n'\sigma'}c^{\dagger}_{n\uparrow}c_{n\downarrow}-
c^{\dagger}_{n\uparrow}c_{n\downarrow}c^{\dagger}_{n'\sigma'}c_{n'\sigma'})=
```
```math
\sum_{\sigma' n'}(-c^{\dagger}_{n'\sigma'}c^{\dagger}_{n\uparrow}c_{n'\sigma'}c_{n\downarrow}+c^{\dagger}_{n'\sigma'}\delta_{\sigma'\uparrow}\delta_{nn'}c_{n\downarrow}+
c^{\dagger}_{n\uparrow}c^{\dagger}_{n'\sigma'}c_{n\downarrow}c_{n'\sigma'}-
c^{\dagger}_{n\uparrow}\delta_{nn'}\delta_{\sigma\downarrow}c_{n'\sigma'})=0
```

Otrzymujemy stąd:
```math
[n,H_{k}]=\sum_{\sigma,n}[n_{n\sigma },n]=0
```
```math
[n,H_{U}]=U\sum_{n}[n,n_{n\uparrow}n_{n\downarrow}]=U\sum_{n}(nn_{n\uparrow}n_{n\downarrow}-n_{n\uparrow}n_{n\downarrow}n)=0
```
```math
[n,H_{t}]=t\sum_{n,\sigma}([n,c_{n\sigma}^{\dagger}c_{n+1,\sigma}]+[c_{n+1,\sigma}^{\dagger}c_{n\sigma}])=0
```
oraz
```math
[n,S_{x}]=\sum_{n}([n,c_{n\uparrow}^{\dagger}c_{n\downarrow}]+[n,c_{n\downarrow}^{\dagger}c_{n\uparrow}])=0
```
```math
[n,S_{y}]=\sum_{n}(-i[n,c_{n\uparrow}^{\dagger}c_{n\downarrow}]+i[n,c_{n\downarrow}^{\dagger}c_{n\uparrow}])=0
```
```math
[n,S_{z}]=\sum_{n}([n,c_{n\uparrow}^{\dagger}c_{n\uparrow}]+[n,c_{n\downarrow}^{\dagger}c_{n\downarrow}])=0
```
skąd
```math
[n,H_{S}]=0
```
```math
[n,H_{12}]=0
```
Dlatego:
```math
[n,H]=0
```
operatory $`H`$ oraz $`n`$ mają wspólną bazę własną, dlatego liczba cząstek jest dobrą liczbą kwantową dla tego układu. Podobnie można pokazać, że o ile $`J=0`$, to także z-towa składowa całkowitego spinu jest także dobrą liczbą kwantową.  

## Diagramy fazowe dla wartości średnich obserwabli

Przedmiotem dalszych rozważań będzie stan termalny układu opisany operatorem gęstości
```math
\rho=\frac{1}{Z}\exp(-\beta H)
```
$`Z`$ jest sumą statystyczną:
```math
Z=Tr[\exp(-\beta H)]
```
Mając dany stan układu w postaci operatora gęsotści można obliczyć wartość oczekiwaną dowolnej obserwabli przez:
```math
\langle A\rangle=Tr(A\rho)
```

W niskiej temperaturze najbardziej prawdopodobny jest stan podstawowy Hamiltonianu. Czym niższa temperatura, tym wartości średnie będą odzwierciedlać dokładnie liczby kwantowe związane ze stanem podstawowym ze względu na znalezione wcześniej elementy symetrii. Bazując na powyższym stwierdzeniu, można wyznaczyć energię stanu podstawowego z diagramu fazowego zalezności wartości oczekiwanych od parametrów energii $`\varepsilon_{1},\varepsilon_{2}`$.


Energie $`\varepsilon_{1},\varepsilon_{2}`$ mierzone są względem poziomu Fermiego. Manipulując tymi wartościami przy zadanych wartościach temperatury,pola oraz parametrów oddziaływań $`U,t,J`$ można otrzymać Hamiltonian dla różnych energii cząstek co przekłada się na zdolność do wzbudzeń.   Poniżej przedstawiono diagramy fazowe przedstawiajace wartości oczekiwane liczby cząstek $`n=\sum_{n,\sigma}c^{\dagger}_{n\sigma}c_{n\sigma}`$, kwadratu spinu $`\vec{S}^{2}`$, z-towej składowej spinu układu $`S_{z}`$ oraz sprzężenia $`\vec{S}_{1}\cdot\vec{S}_{2}`$.

### Diagramy bez sprzężenia ferromagnetycznego

#### Diagram dla $`T=0.01, U=1, t=0, J=0`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/WykresyT0.png?raw=true"/>
</p>

Przy $`t=0`$ granice fazowe są bardzo wyraźne. Na wykresie prezentującym średnią liczbę cząstek można zauważyć, że poniżej energii zerowej dla obu cząstek nie obswerwuje się wzbudzeń co wynika z faktu, iż energię znajdują się poniżej poziomu fermiego, natomiast fluktuacje termalne są niewystarczające do efektywnego wzbudzenia. Z oczywistych względów, także spin układu jest w tym wypadku zerowy. Stopniowe zwiększanie energii jednej z cząstek powoduje pojedyncze wzbudzenie na poziom o spinie $`\langle S_{z}\rangle =1/2`$. Dlasze zwiększanie energii prowadzi do kolejnego wzbudzenia przy wartości $`\varepsilon=U`$ na tym samym poziomie; średnia liczba cząstek wynosi 2. Ze względu na zakaz Pauliego, wzbudzona cząstka musi miec przeciwny spin, aby stan układu pozostawał antysymetryczny, co widoczne jest na wykresie jako obszar $`\langle S_{z}\rangle =0`$. Opisane zachowanie układu znajduje również odzwierciedlenie w Hamiltonianie. Jak zostało wspomniane, człon z $`U`$ odpowiada oddziaływaniu czastek o przeciwnych spinach na tym samym poziomie, w związku z czym po przekroczeniu granicy $`\varepsilon=U`$ dwie cząstki mogą obsadzić pojedynczy stan.

Fragment diagramu, w którym obie energie cząstek znajdują się pomiędzy energią Fermiego, a energią oddziaływania $`U`$ odpowiada pojedynczym obsadzeniom dwóch poziomów. Obie cząstki posiadają spin zgodny z kierunkiem pola magnetycznego, co jest wyraźnie widoczne jako region o wartości  $`\langle S_{z}\rangle =1`$. Dla kolejne pojedyncze wzbudzenia obserwowane są przy przekroczeniu granicy sprzężenia na poszczególnych poziomach. Spin na jendym z poziomów znoszony jest w tym miejscu przez kolejne wzbudzenie, w związku z czym ponownie obserwuje się region z $`\langle S_{z}\rangle =1/2`$. Dla przypadku $`\varepsilon_{1},\varepsilon_{2}>U`$ oba poziomy zostają obsadzone cząstkami o przeciwnym spinie i $`\langle S_{z}\rangle =0`$.

Z powyższego opisu wynika także, że oddziaływanie spinów obydwu cząstek zachodzi wyłącznie w przypadku gdy na dwóch poziomach znajdują się cząstki o spinie skierowanym zgodnie z polem magnetycznym. Na diagramie $`\vec{S}_{1}\cdot\vec{S}_{2}`$ sytuacja ta jest widoczna w obszarze $`0 \lt \varepsilon_{1}\lt U,0\lt\varepsilon_{2} \lt U`$.

Podsumowując powyższe stwierdzenia, otrzymujemy stan podstawowy układu:

<p align="center">

|$`\varepsilon_{1}/U`$|$`\varepsilon_{2}/U`$|$`\|GS\rangle`$|
|---|---|---|
|$`\lt 0 `$|$`\lt 0`$|$`\|0_{\uparrow},0_{\downarrow},0_{\uparrow},0_{\downarrow}\rangle`$| 
</p>

#### Diagram dla $`T=0.01, U=1, t=0.1, J=0`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/Wykresyt0p1.png?raw=true"/>
</p>

#### Diagram dla $`T=0.01, U=1, t=0.2, J=0`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/Wykresyt0p2.png?raw=true"/>
</p>

W przypadku z niezerową wartością całki przeskoku $`t\neq 0`$ granice fazowe ulegają zakrzywieniu. 

### Diagramy ze sprzężeniem ferromagnetycznym

#### Diagram dla $`T=0.01, U=1, t=0.1, J=-0.02`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/Wykresyt0p1J0p02.png?raw=true"/>
</p>

#### Diagram dla $`T=0.01, U=1, t=0.1, J=-0.04`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/Wykresyt0p1J0p04.png?raw=true"/>
</p>

#### Diagram dla $`T=0.01, U=1, t=0.1, J=-0.05`$
<p align="center">
  <img src="https://github.com/JedrekSt/RenormalizacjaWModeluAndersona/blob/main/obrazki/Wykresyt0p1J0p05.png?raw=true"/>
</p>


