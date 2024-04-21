# Analiza dwupozimowego modelu Hubbarda

## Hamiltonian modelu
Hamiltonian rozważanego układu można zapisać jako:

```math
H=\sum_{\sigma=\uparrow,\downarrow}(\varepsilon_{1}c^{\dagger}_{1\sigma}c_{1\sigma}+\varepsilon_{2}c^{\dagger}_{2\sigma}c_{2\sigma})+U\sum_{n=1,2}c_{n\uparrow}^{\dagger}c_{n\uparrow}c_{n\downarrow}^{\dagger}c_{n\downarrow}+t(\sum_{\sigma=\uparrow,\downarrow}c^{\dagger}_{1\sigma}c_{2\sigma}+h.c.)-\vec{S}\cdot\vec{B}-J\vec{S}_{1}\cdot\vec{S}_{2}.
```

- $`\sum_{\sigma=\uparrow,\downarrow}(\varepsilon_{1}c^{\dagger}_{1\sigma}c_{1\sigma}+\varepsilon_{2}c^{\dagger}_{2\sigma}c_{2\sigma})`$ reprezentuje energię kinetyczną na obydwu poziomach sumowaną po dwóch możliwych stanach spinowych
- $`U\sum_{n=1,2}c_{n\uparrow}^{\dagger}c_{n\uparrow}c_{n\downarrow}^{\dagger}c_{n\downarrow}`$ jest energią oddziaływania cząstek o przeciwnym spinie na tym samym poziomie
- $`t(\sum_{\sigma=\uparrow,\downarrow}c^{\dagger}_{1\sigma}c_{2\sigma}+h.c.)`$ jest energią związaną z przeskokami cząstek pomiędzy poziomami bez zmiany spinu
- $`-\vec{S}\cdot\vec{B}`$ jest energią oddziaływania spinów z polem magnetycznym. Operator spinu zdefiniowany jest jako:
```math
\vec{S}=\sum_{n=1,2}\vec{S}_{n}  
```
```math
\vec{S}_{n}=
\frac{\hbar}{2}\left(\begin{array}{c}
c^{\dagger}_{n\downarrow}c_{n\uparrow}+c^{\dagger}_{n\uparrow}c_{n\downarrow}\\
-ic^{\dagger}_{n\downarrow}c_{n\uparrow}+ic^{\dagger}_{n\uparrow}c_{n\downarrow}\\
c^{\dagger}_{n\downarrow}c_{n\downarrow}+c^{\dagger}_{n\uparrow}c_{n\uparrow} \\
\end{array}
\right)
```
- $`-J\vec{S}_{1}\cdot\vec{S}_{2}`$ jest energią oddziaływania spinów na dwóch poziomach

Powyższe fermionowe operatory kreacji i anihilacji spełniają regularne reguły antykomutacji:
```math
\{ c_{n\sigma}^{\dagger},c_{n',\sigma'}^{\dagger} \}=\{ c_{n\sigma},c_{n',\sigma'} \}=0
```
```math
\{ c_{n\sigma},c_{n',\sigma'}^{\dagger} \}=\delta_{nn'}\delta_{kk'}
```
Poziom całkowicie obsadzony zdefiniowany jest przez:
```math
| 1_{\uparrow},1_{\downarrow},1_{\uparrow},1_{\downarrow}\rangle=c_{1\uparrow}^{\dagger}c_{1\downarrow}^{\dagger}c_{2\uparrow}^{\dagger}c_{2\downarrow}^{\dagger}|0_{\uparrow},0_{\downarrow},0_{\uparrow},0_{\downarrow}\rangle
```

## Diagramy fazowe dla wartości średnich obserwabli
