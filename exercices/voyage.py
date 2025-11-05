"""
Exercice de 2 point
"""

from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus, LpBinary, value
from pulp import PULP_CBC_CMD

# Data
villes = ["lyon","saint-etienne","valence","grenoble"]
C = {("lyon","saint-etienne"):26, ("lyon","valence"):34, ("lyon","grenoble"):78,
     ("saint-etienne","lyon"):26, ("saint-etienne","valence"):18, ("saint-etienne","grenoble"):52,
     ("valence","lyon"):34, ("valence","saint-etienne"):18, ("valence","grenoble"):51,
     ("grenoble","lyon"):78, ("grenoble","saint-etienne"):52, ("grenoble","valence"):51}

# Modeling problem
prob = LpProblem("MinimiseDistance",LpMinimize)

# Defining variables
x = LpVariable.dicts("x",[(i,j) for i in villes for j in villes if i!=j],0,1,LpBinary)

# Adding objective function
prob += lpSum(C[(i,j)]*x[(i,j)] for i in villes for j in villes if i != j) # minimiser la distance totale

# Adding constraints
for i in villes:
    prob += lpSum(x[(i,j)] for j in villes if i!=j) == 1 # on sort de toutes les villes
for j in villes:
    prob += lpSum(x[(i,j)] for i in villes if i!=j) == 1 # on entre dans toutes les villes
for i in villes:
    for j in villes:
        if i != j:
            prob += lpSum(x[(i,j)]+x[(j,i)]) <= 1 # pour eviter les cycles entre deux villes
    
#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
# for v in prob.variables():
#     print(f"{v.name}={v.varValue}")

# Showing the circuit
start =  "lyon"
cur = start
for _ in range(len(villes)):
    nexts = [j for j in villes if j!=cur and x[(cur,j)]]
    if not nexts:
        print("No place to go now !")
        break
    next = nexts[0]
    print(f"Going from {cur} -> {next}")
    cur = next
    if cur == "lyon":
        break
    
# Total distance
print(f"Distance totale : {value(prob.objective)}")
