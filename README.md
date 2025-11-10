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
On procède en 2 étapes pour ce problème, d'abord on calcule toutes les combinaisons possibles (n_135,...,n_42) telles que 135\*n_135 + ... + 42\*n_42 <= 300. Cela correspond au nombre de decoupes possibles d'un rouleau de 300cm en les differentes largeurs souhaitées.
Ensuite on definit les variables x_p : le nombre de rouleaux de 300m que l'on decoupe sous le pattern p
On cherche a minimiser la somme des x_p ( le nombre de rouleaux de 300m total )
Commec contrainte on etablit que : 
pour tout type de rouleau ( 135, 108 ,...) s, la somme sur les differents patterns p des x_p*a\[s,p\] >= demande(s) ou a\[s,p\] est le nombre de rouleaux du type s produit par un pattern p
ce qui signifie que pour tout type de rouleau on veut en produire plus ( ou autant ) que le nombre demande.

### Exercice 8 : restaurant (5)
Pour ce problème
### Exercice 7 : restaurant_staffing (5)
On modélise une semaine circulaire (Lun→…→Dim→Lun) avec des blocs 5-on / 2-off.
On établit les variables suivantes : 
* $x_{s,d}\in{0,1}$ : le serveur (s) travaille le jour (d).
* $y_{s,k}\in{0,1}$ : le serveur (s) **démarre** son bloc de 5 jours le jour $k$.
* $u_s\in{0,1}$ : le serveur (s) est utilisé.
* $N\in\mathbb{Z}_+$ : nombre total de serveurs utilisés.
Notre objectif est donc :
* Minimiser $N$.
Et les contraintes sont : 
1. **Compter les serveurs** : $N=\sum_s u_s$
2. **5 jours consécutifs si utilisé** : $\sum_d x_{s,d}=5,u_s$
3. **Un seul début de bloc par serveur utilisé** : $\sum_k y_{s,k}=u_s$
4. **Lien “fenêtre” (mod 7)** :
   $x_{s,k}=\sum_{t=0}^{4} y_{s,(k-t)\bmod 7}\quad\forall s,k$
   (assure 5 jours consécutifs circulaires).
5. **Couverture du besoin** : $\sum_s x_{s,d}\ge \text{Besoin}(d)$ pour chaque jour (d).



