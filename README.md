# Be 1 Recherche opérationnelle et optimisation

### Technical stack : 
- python with pulp
- solver is the default pulp solver which is currently the CBC MILP Solver

Below are the exercises done with the number of points in brackets.
I detailed how I solved the exercise when I felt it was necessary.

### Exercice 1 : monnaie (1)


### Exercice 2 : paysans (3)
On choisit une borne UB sur les jours. 
on definit les variables $y[a,t,d] \in \{0,1\}$  : "(a,t) est fait le jour d"
On doit alors verifier : 
- Affectation : $\sum_{d}^{} y[a,t,d] = 1$ pour tout (a,t).
- Pas de collision outil : pour tout t,d, $\sum_{a}^{} y[a,t,d] ≤ 1$.
- Pas de collision agriculteur : pour tout a,d, $\sum_{t}^{} y[a,t,d] ≤ 1$.
- $D ≥ \sum_{d}^{} d * y[a,t,d]$ pour tout (a,t) ~ D est le plus grand des jours nécessaires
Avec comme objectif min D (min le nombre de jours).

### Exercice 3 : gâteaux (2)
On doit répondre a la question : combien de tarte le pâtissier doit il faire avec ses stocks et de quels types sont les tartes.
On modèlise avec comme fonction objectif le gain total : prix_tarte1*quantité_tarte1 + ...
Comme contrainte on a que le somme totale des ingrédients utilisés par les tartes ne peut être supérieur à la quantité total de de chaque ingrédient.


### Exercice 4 : voyage (2)

### Exercice 5 : coloration (2)

### Exercice 6 : decoupe_papier (2)
On procède en 2 étapes pour ce problème, d'abord on calcule toutes les combinaisons possibles (n_135,...,n_42) telles que 135\*n_135 + ... + 42\*n_42 <= 300. 
Cela correspond au nombre de decoupes possibles d'un rouleau de 300cm en les differentes largeurs souhaitées.
Ensuite on definit les variables x_p : le nombre de rouleaux de 300m que l'on decoupe sous le pattern p
On cherche a minimiser la somme des x_p ( le nombre de rouleaux de 300m total )
Commec contrainte on etablit que : 
pour tout type de rouleau ( 135, 108 ,...) s, la somme sur les differents patterns p des x_p*a\[s,p\] >= demande(s) ou a\[s,p\] est le nombre de rouleaux du type s produit par un pattern p
ce qui signifie que pour tout type de rouleau on veut en produire plus ( ou autant ) que le nombre demande.

### Exercice 7 : restaurant (5)
Pour ce problème : on modélise une semaine circulaire (Lun→…→Dim→Lun) avec des blocs 5-on / 2-off.
On établit les variables suivantes : 
* $x_{s,d}\in{0,1}$ : le serveur (s) travaille le jour (d).
* $y_{s,k}\in{0,1}$ : le serveur (s) **démarre** son bloc de 5 jours le jour $k$.
* $u_s\in{0,1}$ : le serveur (s) est utilisé.
* $N\in\mathbb{Z}_+$ : nombre total de serveurs utilisés.
Notre objectif est donc :
* Minimiser $N$.

Et les contraintes sont : 
1. *Compter les serveurs* : $N=\sum_s u_s$
2. *5 jours consécutifs si utilisé*: $\sum_d x_{s,d}=5,u_s$
3. *Un seul début de bloc par serveur utilisé* : $\sum_k y_{s,k}=u_s$
4. *Lien “fenêtre” (mod 7)* :
   $x_{s,k}=\sum_{t=0}^{4} y_{s,(k-t)\bmod 7}\quad\forall s,k$
   (assure 5 jours consécutifs circulaires).
5. *Couverture du besoin* : $\sum_s x_{s,d}\ge \text{Besoin}(d)$ pour chaque jour (d).

### Exercice 8 : financement (3)

**Idée & modélisation.**
Placer 1000€ sur 6 ans en maximisant le capital final. On modélise l’année $t=1..6$ et le capital disponible $g_t$, avec des variables d’investissement $x_{i,t}$ (montant placé dans l’actif $i$ à l’année $t$), et des retours $y_{i,\tau}$ encaissés à l’année $\tau=t+k_i$ selon la durée d’immobilisation $k_i$. Contrainte de disponibilité des produits ($o2$ indisponible en $t=1,3$; $o3$ seulement en $t=1$; $o1$ à $12%$ si $t=1$, sinon $11%$). Conservation des flux :

* $r_t = g_t - \sum_i x_{i,t}$ (trésorerie non investie),
* $g_{t+1} = r_t + \sum_i y_{i,t+1}$,
* $G = g_7$ (objectif à maximiser), $g_1=1000$.
  Pour éviter l’**unbounded**, on force $y_{i,\tau}=0$ quand $(i,\tau)$ **ne peut pas** provenir d’un placement autorisé (filtrage par horizon et disponibilités).

**Résolution & lecture du plan.**
Le modèle renvoie *Optimal*. Le plan optimal (flux) suit une chaîne “placer → encaisser → replacer” en respectant les fenêtres d’achat/échéance :

* $t=1$ : placer tout sur **o1** (cas spécial $12%$ sur $2$ ans) → encaissement en $t=3$.
* $t=3$ : replacer en **ca** ($5%$ sur $1$ an) → encaissement en $t=4$.
* $t=4$ : placer en **o2** ($18%$ sur $3$ ans, disponible) → encaissement final en $t=7$.
  Capital final $G \approx 1387{,}68,€$.

**Bilan & taux moyen.**
Croissance globale $1387{,}68/1000$ sur $6$ ans $\Rightarrow$ taux annuel moyen $\approx 5{,}61%$, **légèrement supérieur** au $5%$ de la caisse d’épargne, grâce au timing des obligations plus rémunératrices quand elles sont disponibles.




