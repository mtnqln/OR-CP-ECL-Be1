"""
Exercice de 2 point
"""

from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus, value
from pulp import PULP_CBC_CMD

# Data
roul = ["135cm","108cm","93cm","42cm"] # rouleaux a faire
qt =  {"135cm":97,"108cm":610,"93cm":395,"42cm":211}# quantites
size = {"3m":300,"135cm":135,"108cm":108,"93cm":93,"42cm":42}
L = 300

# generation de tous les pattern de decoupes possibles verifiant leur somme < 300cm
patterns = []
for a in range(L // size["135cm"]+1):
    for b in range(L // size["108cm"]+1):
        for c in range(L // size["93cm"]+1):
            for d in range( L // size["42cm"]+1):
                total = a*135 + b*108 + c*93 + d*42
                if 0< total <= 300:
                    patterns.append({"135cm": a, "108cm": b, "93cm": c, "42cm": d})


# Modeling problem
prob = LpProblem("MyProblem",LpMinimize)

# Defining variables
x = {p:LpVariable(f"x_{p}",0,None,LpInteger) for p in range(len(patterns))} # x_p est le nombre de rouleaux de 300cm que l'on decoupe suivant le pattern p

# Adding objective function
prob += lpSum(x[i] for i in x.keys()) #on minimise le nombre total de rouleaux de 300cm

# Adding constraints
for s in roul:
    prob += lpSum(x[p]*patterns[p][s] for p in range(len(patterns))) >= qt[s] # on verifie que pour tout type de rouleau le nombre total produit est bien superieur a la demande


#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
print(f"On produit {value(prob.objective)} rouleaux de 3m")
for v in prob.variables():
    if v.value() != 0:
        print(f"{v.name}={v.varValue}")
        print(f"Soit on decoupe {v.varValue} rouleaux de 3m en : {patterns[int(v.name[2:])]}")