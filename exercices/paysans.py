"""
Exercice de 3 points
"""
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus, LpBinary
import pandas as pd

# Data
agri = ["M","P","C"] # agriculteurs
tools = ["H","M","B","T"] # outils
pref = {"M":["H","T","M","B"], # preferences
        "P":["T","M","H","B"],
        "C":["M","T","B","H"]
        }
UB = len(agri)*len(tools)+1 # upper bound for days 
days = list(range(1,UB)) # days
agri_tools_days_tuple = [(a,t,d) for a in agri for t in tools for d in days] # tuple (agri,tool,day) for all combinations

# modeling problem
prob = LpProblem("Paysans",LpMinimize)

# Variables
D = LpVariable("MaxDay",1,UB,LpInteger) # Number of days needed 
y = LpVariable.dicts("BinaryVariable",agri_tools_days_tuple,0,1,LpBinary) # Each tuple is either 0 or 1, for a (agri,tool,day) if value is 1 => agri uses tool on day 

# objective function is added
prob += D, "Number of days needed"

# constraints
for (a,tool,_) in agri_tools_days_tuple:
    prob += lpSum(y[a,tool,d] for d in days) == 1 # Tous les outils sont utilises par tous les agri

for (_,tool,day) in agri_tools_days_tuple:
    prob+= lpSum(y[a,tool,day] for a in agri) <= 1 #  Un outil utilise par l’un ne peut etre utilise le meme jour par un autre

for (a,_,day) in agri_tools_days_tuple:
    prob += lpSum(y[a,t,day] for t in tools) <= 1# Un agriculteur utilise chaque outil toute une journee

# constraints on preferences
for a in pref.keys():
    for d in days:
        if len(pref[a])>1:
                for index in range(len(pref[a])-1):
                        prob += y[a,pref[a][index],d] >= y[a,pref[a][index+1],d] # indexed by +1 and +2 because days start at 1
                pref[a].pop(0)
for a in agri:
    for t in tools:
        prob += lpSum(d*y[a,t,d] for d in days) <= D # To find the smallest D 

# solve
prob.solve()

# Result
print(f"Status : {LpStatus[prob.status]}")
print(f"Number of days : {D.value()}")

# Showing result as a matrix
day_of = {
    (a,t): int(sum(d * y[(a,t,d)].value() for d in days))
    for a in agri for t in tools
}
df = pd.DataFrame({t: [day_of[(a,t)] for a in agri] for t in tools}, index=agri)

print(df.map(lambda d: f"j {d}").to_string()) #type: ignore




