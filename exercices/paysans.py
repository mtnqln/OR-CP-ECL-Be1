"""
Exercice de 3 points
"""
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus

# Data
agri = ["M","P","C"] # agriculteurs
tools = ["H","M","B","T"] # outils
pref = {"M":["H","T","M","B"], # preferences
        "P":["T","M","H","B"],
        "C":["M","T","B","H"]
        }

# modeling problem
prob = LpProblem("Paysans",LpMinimize)

# Variables
agri_tool_pairing = [(a,t) for a in agri for t in tools]
days = LpVariable.dicts("day",agri_tool_pairing,0)

prob += lpSum([days[pair] for pair in agri_tool_pairing])," Number of days"