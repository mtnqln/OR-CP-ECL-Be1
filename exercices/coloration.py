"""
Exercice de 2 point
"""

from pulp import LpProblem, LpMinimize, LpVariable, LpBinary, lpSum, LpStatus, LpInteger, value
from pulp import PULP_CBC_CMD

# Data
S = {"A","B","C","D","E","F"}
V = {
    ("A","B"), ("A","C"), ("A","D"), ("A","E"), ("A","F"),
    ("B","C"), ("B","D"), ("B","F"),
    ("C","D"), ("C","E"),
    ("D","E"), ("D","F"),
    ("E","F"),
} 
Adj = {
    ("A","B"),("A","F"),("B","C"),("C","D"),("D","E"),("E","F"),

}

G = (S,V) # graph non orienté

UB = len(S)
colors = list(range(UB)) # colors, starting with one color per node
noeud_et_couleurs = [(n,c) for n in S for c in colors]
# Modeling problem
prob = LpProblem("MyProblem",LpMinimize)


# Defining variables
x = LpVariable.dicts("Noeud",noeud_et_couleurs,0,1,LpBinary)
MC = LpVariable("MaxColors",1,None,LpInteger) # Max colors
y = LpVariable.dicts("ColorUsed", colors, 0, 1, LpBinary)

# Adding objective function
prob+= MC # minimizing the number of colors

# Adding constraints
for s1,s2 in Adj:
    for c in colors:
        prob += x[s1,c] + x[s2,c] <= 1 # deux noeuds connectes ne recoivent jamais la meme couleur

for s in S:
    prob+= lpSum(x[s,c] for c in colors) == 1 # un noeud doit avoir une couleur

for c in colors:
    for s in S:
        prob+=x[s,c] <=y[c] #variable tqui compte le nombre de couleurs differentes

prob += lpSum(y[c] for c in colors) <= MC # contrainte sur le nombre max de couleur

#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
for v in prob.variables():
    if v.varValue == 1.0:
        print(f"{v.name}={v.varValue}")
print(f"Number of colors used : {value(prob.objective)}")