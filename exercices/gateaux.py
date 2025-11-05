"""
Exercice de 2 points
"""

from pulp import LpProblem, LpMaximize, LpVariable, LpInteger, lpSum, LpStatus, value
from pulp import PULP_CBC_CMD

# Data
tartes = ["TarteChocolat","TarteBanane"]
ingredients = ["farine","banane","sucre","beurre","cacao"]
prices = {
    "TarteChocolat":4.5,
    "TarteBanane":4.0
}
recipes = {
    "TarteChocolat":{"farine":200,"cacao":75,"sucre":150,"beurre":150},
    "TarteBanane":{"farine":250,"banane":2,"sucre":75,"beurre":100}
}
stock = {
    "farine":4000, # grammes
    "banane":6, #nombre de bananes
    "sucre":2000, # grammes
    "beurre":500, #grammes
    "cacao":500 #grammes
}

# Modeling problem
prob = LpProblem("MaximiseChiffreAffaire",LpMaximize)

# Defining variables
nombre_tartes = LpVariable.dicts("NombreTartes",tartes,0,None,LpInteger) # un type de variable pour chaque type de tarte

# Adding objective function
prob += lpSum(prices[i]*nombre_tartes[i] for i in tartes), "Total price"

# Adding constraints
for ingr in stock:
    prob += lpSum(recipes[t][ingr]*nombre_tartes[t] for t in tartes if ingr in recipes[t].keys()) <= stock[ingr] # on ne peut pas utiliser plus d'ingredient qu'il y en a au total


#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}") # resultat
for v in prob.variables():
    print(f"{v.name}={v.varValue}") # combien de chaque tartes
print(f"\n Gain total : {value(prob.objective)}$") # gain total