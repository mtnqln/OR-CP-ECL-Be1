# Be 1 Recherche opérationnelle et optimisation

### Outils utilisés : 
- python avec pulp
- Le solver est le solver pulp par défault qui est le CBC MILP Solver

Ci-dessous sont les exercices du be, j'ai détaillé quand j'ai jugé cela nécessaire.

---

### Exercice 1 : monnaie (1)

---

### Exercice 2 : paysans (3)

**Modélisation.**
On se donne un horizon $H$ (borne supérieure sur les jours, p.ex. $H=\text{UB}$).
Variables binaires $y[a,t,d]\in{0,1}$ : “la tâche $t$ de l’agriculteur $a$ est réalisée le jour $d$”, pour $a\in A$, $t\in T_a$, $d\in{1,\dots,H}$.
Variable entière $D$ : dernier jour utilisé (makespan).

**Contraintes.**

* **Affectation (exactement un jour par tâche)** :
  $\displaystyle \sum_{d=1}^{H} y[a,t,d] = 1 \quad \forall(a,t).$
* **Pas de collision outil (au plus une tâche de type $t$ par jour)** :
  $\displaystyle \sum_{a} y[a,t,d] \le 1 \quad \forall(t,d).$
* **Pas de collision agriculteur (au plus une tâche par agriculteur et par jour)** :
  $\displaystyle \sum_{t} y[a,t,d] \le 1 \quad \forall(a,d).$
* **Définition du makespan** :
  $\displaystyle D \ge \sum_{d=1}^{H} d,y[a,t,d] \quad \forall(a,t).$

**Objectif.**
Minimiser le nombre de jours : $\displaystyle \min D$.

---

### Exercice 3 : gâteaux (2)

**Problème.** Déterminer combien de tartes produire (et de quels types) en respectant les stocks d’ingrédients, afin de maximiser le gain.
**Modélisation.**
* Variables : $x_k \ge 0$ = nombre de tartes du type $k$.
* Objectif : maximiser $ \sum_k p_k,x_k$ (où $p_k$ est le prix/marge de la tarte $k$).
* Contraintes d’ingrédients : pour chaque ingrédient $i$,
  $\displaystyle \sum_k a_{ik},x_k \le \text{stock}*i$,
  où $a*{ik}$ est la quantité de l’ingrédient $i$ requise par une tarte $k$.
* (Optionnel) Intégralité : $x_k \in \mathbb{Z}_+$.
**Sortie attendue.** Quantités optimales par type de tarte et profit maximal, sous contraintes de stock.

---

### Exercice 4 : voyage (2)

**Idée.**
Trouver une tournée qui passe **une fois** par chaque ville et revient au départ en **minimisant** la distance totale (TSP dirigé).

**Modélisation.**

* Variables : $x_{ij}\in{0,1}$ pour $i\neq j$, vaut $1$ si l’on va de $i$ vers $j$.
* Objectif : $\min \displaystyle\sum_{i}\sum_{j\ne i} C_{ij},x_{ij}$.

**Contraintes.**

* **Degré sortant** (quitter chaque ville une fois) : $\displaystyle\sum_{j\ne i} x_{ij}=1\quad\forall i$.
* **Degré entrant** (entrer dans chaque ville une fois) : $\displaystyle\sum_{i\ne j} x_{ij}=1\quad\forall j$.
* **Élimination des sous-tours** (indispensable, la contrainte “pas de 2-cycle” ne suffit pas) :

  * *Version MTZ* (ajout de variables d’ordre $u_i$) : pour $i\ne j$,
    $u_i - u_j + n,x_{ij}\le n-1$, avec $1\le u_i\le n$ et fixer $u_{\text{départ}}=1$.
  * *(Ou)* *SEC* : pour tout sous-ensemble non vide $S\subset V$,
    $\displaystyle\sum_{i\in S}\sum_{j\in S,,j\ne i} x_{ij} \le |S|-1$.

**Lecture de solution.**
Suivre les arcs $x_{ij}=1$ depuis la ville de départ pour reconstruire la tournée (une arête sortante et une entrante par ville).

---

### Exercice 5 : coloration (2)

**Idée.**
Colorer les sommets d’un graphe non orienté de sorte que deux sommets adjacents n’aient jamais la même couleur, en **minimisant** le nombre de couleurs utilisées (trouver le nombre chromatique).

**Modélisation (ILP).**

* Variables :

  * $x_{s,c}\in{0,1}$ : vaut $1$ si le sommet $s\in S$ reçoit la couleur $c$.
  * $y_c\in{0,1}$ : vaut $1$ si la couleur $c$ est utilisée par au moins un sommet.
  * $MC\in\mathbb{Z}_+$ : nombre total de couleurs utilisées.
* Objectif : $,\min\ MC$.

**Contraintes.**

* **Conflit sur les arêtes** : pour toute arête $(u,v)\in E$ et toute couleur $c$,
  $x_{u,c}+x_{v,c}\le 1$ (deux sommets adjacents ne partagent pas la même couleur).
* **Affectation d’une couleur par sommet** : pour tout $s\in S$,
  $\sum_{c} x_{s,c}=1$.
* **Activation des couleurs** : pour tout $s,c$,
  $x_{s,c}\le y_c$ (si une couleur est assignée, elle est marquée comme utilisée).
* **Comptage des couleurs** : $\sum_{c} y_c = MC$.

**Sortie attendue.**
Une affectation $(x_{s,c})$ réalisable et minimale, et la valeur $MC$ (nombre de couleurs utilisées).

---

### Exercice 6 : découpe_papier (2)

**Idée.** Problème de cutting stock : découper des rouleaux de $300$ cm pour satisfaire la demande en largeurs ${135,108,93,42}$ en utilisant le minimum de rouleaux sources.

**Modélisation par patterns.**

1. Énumérer les schémas (patterns) $p$ : quadruplets $(n_{135},n_{108},n_{93},n_{42})$ tels que
   $135,n_{135}+108,n_{108}+93,n_{93}+42,n_{42}\le 300$.
2. Variables : $x_p \in \mathbb{Z}_+$ = nombre de rouleaux de $300$ cm découpés selon le pattern $p$.
3. Objectif : $\min \sum_p x_p$ (nombre total de rouleaux sources).
4. Couverture de la demande : pour chaque largeur $s\in{135,108,93,42}$,
   $\displaystyle \sum_p a_{s,p},x_p \ge \text{demande}(s)$,
   où $a_{s,p}$ est le nombre de morceaux de largeur $s$ produits par le pattern $p$.

**Sortie attendue.** Nombre minimal de rouleaux de $300$ cm et répartition par patterns (découpe à effectuer).

---

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

---

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

---

### Exercice 9 : infirmieres (5)

**Idée & modélisation.**
Trouver un planning hebdomadaire valide (problème de satisfaction) pour 4 infirmières ($i$), 3 shifts ($s$) et 7 jours ($j$). On modélise l’affectation par $x_{i,s,j}=1$ si l’infirmière $i$ prend le shift $s$ le jour $j$. Contraintes principales : $\ge 5$ jours/semaine, $\le 1$ shift/jour.
La difficulté est la contrainte de **2 infirmières *distinctes* par shift**. On la modélise avec une variable auxiliaire $y_{i,s}=1$ si $i$ travaille *au moins un jour* sur $s$. On lie les variables via "Big-M" : $\sum_j x_{i,s,j} \le M \cdot y_{i,s}$ (force $y=1$ si $\sum x \ge 1$) et $y_{i,s} \le \sum_j x_{i,s,j}$ (force $y=0$ si $\sum x = 0$).

**Contraintes & résolution.**
D'autres contraintes gèrent les jours consécutifs : interdiction $s_1 \to s_2$ (jours $j$, $j+1$) et obligation de blocs $\ge 2$ jours sur S2/S3 (modélisé par "pas de jour isolé" : $x_{j} \le x_{j-1} + x_{j+1}$). Toutes les contraintes de jours adjacents doivent gérer la boucle Dimanche $\to$ Lundi (via modulo). Le modèle n'a pas d'objectif (maximisation) et renvoie *Optimal* s'il trouve une solution.

**Bilan.**
Le modèle trouve un planning *faisable*. La complexité réside dans la dissociation entre l'affectation journalière ($x_{i,s,j}$) et la présence hebdomadaire ($y_{i,s}$), qui est la clé pour compter les infirmières distinctes par shift.




