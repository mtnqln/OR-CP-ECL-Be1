"""
Exercice de 3 point
"""

from pulp import LpProblem, LpMaximize, LpVariable, LpInteger, lpSum, LpStatus, value, LpBinary, LpContinuous
from pulp import PULP_CBC_CMD

# Data
S = 1000
I = ["ca","o1","o2","o3"]
taux = {"ca":(5/100,1),"o1":(11/100,2),"o2":(18/100,3),"o3":(24/100,4)} # tuple (taux,temps d'immobilisation)
T_capital = list(range(1, 8)) # Années 1 à 7
T_invest = list(range(1, 7))  # Années 1 à 6
Ty = list(range(2,8)) #range de 2 a 7
# Modeling problem
prob = LpProblem("MyProblem",LpMaximize)

# Defining variables
G = LpVariable("Gain",0,None,LpContinuous) # gain
g = LpVariable.dicts("gainActuel",T_capital,0,None,LpContinuous) # Capital disponible en debut d'annee t
y = LpVariable.dicts("RetourSurInvestissement",[(i,ty) for i in I for ty in Ty],0,None,LpContinuous) # gain des investissements i que l'on recupere a t
x = LpVariable.dicts("Investissement",[(i,t) for i in I for t in T_invest],0,None,LpContinuous) #quantite de capital que l'on investit a l'annee t dans l'actif i
r = LpVariable.dicts("ResteNonInvesti",[t for t in T_invest],0,None,LpContinuous) # ce qui n'est pas investi a la fin de l'annee t

# Adding objective function
prob += G

# Adding constraints
prob += g[7] == G # le gain de la 6e annee est le gain recuperé
prob += g[1] == 1000 # on commence avec 1000 euros

for t in T_invest:
    prob += r[t] == g[t] - lpSum(x[i,t] for i in I) # ce qui n'est pas investi a la fin de l'annee t c'est ce qu'on avait au debut - ce qui a ete investi

for t in T_invest:
    prob += g[t] >= lpSum(x[i,t] for i in I) # on ne peut pas investir plus a l'annee t que ce que l'on detient en debut d'annee

for t in Ty:
    prob += g[t] == lpSum(y[i,t] for i in I) + r[t-1] # la somme que l'on detient pour investir en debut d'annee t+1 c'est la somme que l'on recupere des investissements a t+1 + ce que l'on avait pas investi l'annee precedente

for i in I:
    for t in T_invest:
        k = taux[i][1] # nombre d'annee d'immobilisation
        if  k + t > 7:
            prob += x[i,t] == 0 # si l'investissement n'est pas recupere apres 6 ans ( au debut de la 7e annee ) on investit pas
        elif i=="o1" and t == 1:
            prob += y[i,t+2] == (1.12) * x[i,t] # condition sur o1 si on investit la premiere annee
        elif i=="o2" and (t == 1 or t == 3):
            prob += x[i,t] == 0 # on ne peut investir dans o2 la 1ere et 3e annee
        elif i=="o3" and t != 1:
            prob += x[i,t] == 0 # on ne peut investir dans o3 que la premiere annee
        else :
            prob += y[i,t+k] == (1+taux[i][0]) * x[i,t] # combien on recupere apres avoir investit k annee

# tous les retours sur investissements possibles ( certains doivent etre nuls car ils ne peuvent etre le retour d'aucun investissement )
retour_possible = set()
for i in I:
    k=taux[i][1]
    for t in T_invest:
        if i=="o2" and (t == 1 or t == 3):
            continue # pas d'investissement possible dondc pas de retour sur investissement a partir de cet investssement
        if i=="o3" and t != 1:
            continue # pas d'investissement possible dondc pas de retour sur investissement a partir de cet investssement
        else:
            ty = k +t
            if ty <= 7:
                retour_possible.add((i,ty)) # on ajoute les couples ou le retour sur investissement est possible

for i in I:
    for t in Ty:
        if (i,t) not in retour_possible:
            prob += y[i,t] == 0 # aucun retour sur investissement possible


#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
print(f"Objective function value : {value(prob.objective)}")
for v in prob.variables():
    if v.value() != 0 and "Investissement" in v.name:
        print(f"{v.name}={v.varValue}")
rendement = ((value(prob.objective)/1000)**(1/6) - 1)*100
print(f"Rendement  : {rendement}%")
print(f"Soit : {rendement/5} fois plus grand que celui de la caisse d'epargne")