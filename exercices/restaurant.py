"""
Exercice de 5 point
"""

from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus, LpBinary, value
from pulp import PULP_CBC_CMD
import pandas as pd

# Data
days = ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"]
Besoin = {"Lun":14,"Mar":13,"Mer":15,"Jeu":16,"Ven":19,"Sam":18,"Dim":11}
D = sum(v for v in Besoin.values()) # taking a upper bound for the number of servers
rangeD = range(D)

# Modeling problem
prob = LpProblem("MyProblem",LpMinimize)

# Defining variables
x = LpVariable.dicts("Serveur",[(s,d) for s in range(D) for d in days],0,1,LpBinary) # on definit une variable x[i,j] dans 0,1 ou i est le serveur j le jour est 0 si il ne travaille pas et 1 si il travaille
y = LpVariable.dicts("BlocTravaille",[(s,k) for s in rangeD for k in days],0,1,LpBinary) # variable indiquant si le serveur i commence son bloc de 5j le jour k
u = LpVariable.dicts("ServeurEstUtilise",[s for s in rangeD],0,1,LpBinary) # Si un serveur est utilise
N = LpVariable("NumberOfServeurs",0,None,LpInteger)

# Adding objective function
prob += N # on minimise le nombre de serveurs

# Adding constraints
prob += N == lpSum(u[s] for s in rangeD)

for s in rangeD:
    prob += lpSum(x[(s,j)] for j in days) == 5*u[s] # un serveur travaille 5J ou ne travaille pas

for (d,v) in Besoin.items():
    prob += lpSum(x[(i,d)] for i in rangeD) >= v # au moins 14 serveurs travaillent le lundim 13 le mardi ...

for s in rangeD:
    prob += lpSum(y[s,d] for d in days) == u[s] # un travailleur travaille un bloc de 5j

for s in rangeD:
    for k in range(len(days)):
        prob += x[s,days[k]] == lpSum(y[s,days[j]] for j in range(k,k-5,-1))

#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))


#Solution and status
print(f"Status : {LpStatus[prob.status]}")
print(f"On a besoin de : {value(prob.objective)} serveurs !")

r:dict[int,list[float]] = {}
for s in rangeD:
    total = sum(x[s,j].value() for j in days)
    if total >0.0:
        for j in days:
            r[s] = [x[s,j].value() for j in days] 
df = pd.DataFrame.from_dict(data=r,orient='index')
df.columns = days

print(f"Planning : \n {df.head(n=int(value(prob.objective)))}")
