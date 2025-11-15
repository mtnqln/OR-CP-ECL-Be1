"""
Exercice de 5 point
"""

from pulp import LpProblem, LpMaximize, LpVariable, LpInteger, lpSum, LpStatus, value, LpBinary
from pulp import PULP_CBC_CMD
import pandas as pd

# Data
A = ["A","B","C","D"] # ateliers
O = ["Op1","Op2","Op3","Op4"] # operateurs
C = {"A":5,"B":3,"C":2,"D":3} # capacites de production
S = {"Op1":(8,13),"Op2":(8,13),"Op3":(9,13),"Op4":(10,15)} # horaires par ouvrier
H = list(range(8,16)) # tous les horaires possibles de 8h a 15h
N = 30 # nombre de vehicules

# Modeling problem
prob = LpProblem("MyProblem",LpMaximize)

# Adding variables
x = LpVariable.dicts("Operateur_Atelier_Horaire",[(o,a,h) for o in O for a in A for h in H],0,1,LpBinary) # 1 si l'operateur o travaille dans l'atelier a pendant l'heure h
g = LpVariable.dicts("Flux_Atelier_Horaire",[(a,h) for a in A for h in H],0,N,LpInteger) # flux de voiture qui vont dans l'atelier a pendant l'horaire h
G = LpVariable.dicts("Voiture_finie_Heure",H,0,N,LpInteger) # nombre de voiture qui sortent a l'heure h

# Adding objective function
prob += lpSum(G[h] for h in H),"MaximiserNombreVoiture"

# Adding constraints
prob += lpSum(g["A",h] for h in H) <= N # on dispose de N=30 vehicule au total
prob += g["B",8] == 0 # pas de vehicules devant les autres ateliers a 8h
prob += g["C",8] == 0
prob += g["D",8] == 0

for o in O:
    for h in H:
        prob += lpSum(x[o,a,h] for a in A ) <= 1 # un operateur est dans un seul endroit a la fois
for h in H[1:]:
    prob += G[h] == g["D",h-1] # le nombre de vehicule sortis a l'heure h est le nombre de vehicule qui etait dans le dernier atelier a h-1
for h in H[:4]:
    prob += G[h] == 0 # les 4 premieres heures aucune voiture n'a pu atteindre la sortie
for a in A:
    for h in H:
        prob += g[a,h] <= lpSum(C[a]*x[o,a,h] for o in O) #le flux de voiture qui traverse chaque usine est inferieur ou egale a la capacite de production de l'usine
for h in H[1:]:
    for index,_ in enumerate(A[1:]):
        prob += g[A[index+1],h] <= g[A[index],h-1] # on produit forcement autant ou moins que le stock qui nous a ete livre de l'atelier precedent produit pendant l'heure precedente

for o in O:
    horaire = list(range(S[o][0],S[o][1]))  #horaire des ouvriers
    for h in H:
        if h in horaire:
            prob += lpSum(x[o,a,h] for a in A) == 1 # travaille dans ses horaires
        else:
            prob += lpSum(x[o,a,h] for a in A) == 0 # ne travaille pas en dehors de ses horaires

#Solving problem
prob.solve(PULP_CBC_CMD(msg=False))

#Solution and status
print(f"Status : {LpStatus[prob.status]}")
print(f"Vehicule passés dans les 4 ateliers : {value(prob.objective)}")
# for v in prob.variables():
#     if v.varValue !=0.0:
#         print(f"{v.name}={v.varValue}")
other_df = pd.DataFrame(columns=H,index=A)
df = pd.DataFrame(columns=H,index=A)
df = df.map(lambda _: [])
for h in H:
    for a in A:
        if g[a,h].varValue != 0.0:
            other_df.loc[a,h] = g[a,h].varValue
        for o in O:
            if x[o,a,h].varValue == 1.0:
                df.loc[a,h].append(o) #type: ignore

print(f"Organisation : \n {df.head()}")
print(f"Production de voiture : \n {other_df.head()}")
