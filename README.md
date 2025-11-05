# Be 1 Recherche opérationnelle et optimisation

### technical stack : 
- python with pulp
- solver is the default pulp solver which is currently the CBC MILP Solver

Below are the exercises done with the number of points in brackets.
I detailed how I solved the exercise when I felt it was necessary.

### exercice 1 : monnaie (1)


### exercise 2 : paysans (3)
On choisit une borne UB sur les jours. 
on definit les variables $y[a,t,d] \in \{0,1\}  : "(a,t) est fait le jour d"
On doit alors verifier : 
- Affectation : $\sum_{d}^{} y[a,t,d] = 1$ pour tout (a,t).
- Pas de collision outil : pour tout t,d, $\sum_{a}^{} y[a,t,d] ≤ 1$.
- Pas de collision agriculteur : pour tout a,d, $\sum_{t}^{} y[a,t,d] ≤ 1$.
- $D ≥ \sum_{d}^{} d * y[a,t,d]$ pour tout (a,t) ~ D est le plus grand des jours nécessaires
Avec comme objectif min D (min le nombre de jours).

### exercise 3 : gâteaux (2)
On doit répondre a la question : combien de tarte le pâtissier doit il faire avec ses stocks et de quels types sont les tartes.
On modèlise avec comme fonction objectif le gain total : prix_tarte1*quantité_tarte1 + ...
Comme contrainte on a que le somme totale des ingrédients utilisés par les tartes ne peut être supérieur à la quantité total de de chaque ingrédient.


