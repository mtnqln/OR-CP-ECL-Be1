"""
Exercice de 1 point
"""

from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus

# Data
M = 39 # Montant
S = [1,7,23] # Stock de pieces

# Modeling problem
prob = LpProblem("Monnaie",LpMinimize)

# Defining variables
stack = LpVariable.dicts("pieces",S,0,None,LpInteger)

# Adding objective function
prob += lpSum([stack[i] for i in S]), "Total number of pieces"

# Adding constraints
prob += lpSum([i*stack[i] for i in S]) == M

#Solving problem
prob.solve()

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
for v in prob.variables():
    print(f"{v.name}={v.varValue}")

