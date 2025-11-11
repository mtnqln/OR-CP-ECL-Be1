"""
Exercice de 5 point
"""

from pulp import LpProblem, LpVariable, LpInteger, lpSum, LpStatus, value, LpBinary
from pulp import PULP_CBC_CMD
import pandas as pd

# Data
J = ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"] # jours
S = [1,2,3] # shifts
I = ["A","B","C","D"] # infirmieres
M = len(J) # 7


# Modeling problem
prob = LpProblem("MyProblem")

# Defining variables
x = LpVariable.dicts("Inf_Shift_Jour",[(i,s,j) for i in I for s in S for j in J],0,1,LpBinary) # variable pour dire si une infirmiere i travaille le shift s au jour j
y = LpVariable.dicts("Inf_Shift",[(i,s) for i in I for s in S],0,1,LpBinary) # si une infirmiere travaille au shift s dans la semaine

# Adding objective function
# Pas de fonction objectif ici

# Adding constraints
for s in S:
    for j in J:
        prob += lpSum(x[i,s,j] for i in I) == 1 # un shift est pris par une infirmiere

for i in I:
    prob += lpSum([x[i,s,j] for s in S for j in J]) >= 5 # une infirmiere travaille au moins 5j dans la semaine
for i in I:
    for j in J:
        prob+= lpSum(x[i,s,j] for s in S) <= 1 # un shift par jour

for i in I:
    for index,j_actuel in enumerate(J):
        j_suivant = J[(index+1) % M]
        j_avant = J[(index-1)%M]
        for s in S[1:]:
            prob += x[i,s,j_actuel] <= x[i,s,j_avant] + x[i,s,j_suivant] # au shift 2 ou 3 on travaille au moins 2 jours d'affiles
        
        for s1 in S:
            for s2 in S:
                if s1 != s2:    
                    prob += x[i,s1,j_actuel] + x[i,s2,j_suivant] <= 1 # une infirmiere ne peut pas travailler deux shifts differents sur 2 jours consecutifs

for s in S:
    prob += lpSum(y[i,s] for i in I) == 2 # un shift contient deux infirmieres differentes par semaine

for i in I:
    for s in S:
        prob += lpSum(x[i,s,j] for j in J) <= M*y[i,s] # condition pour lier y et x : la somme des jours travailles pour un shift et une infirmiere est inferieur au nombre de jours max travailles possibles (7)
        prob += y[i,s] <= lpSum(x[i,s,j] for j in J) # condition pour lier y et x : y est inferieur a la somme des x sur les jours pour une infirmiere + 1 shift fixé

#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
# for v in prob.variables():
#     print(f"{v.name}={v.varValue}")

df = pd.DataFrame(index=S,columns=J)
for j in J:
    for s in S:
        for i in I:
            if x[i,s,j].varValue == 1.0:
                df.loc[s,j] = i
print(f"Infirmieres : {I}")
print(f"Organisation : \n {df.head()}")
