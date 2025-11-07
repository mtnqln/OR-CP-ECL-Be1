\* MyProblem *\
Minimize
OBJ: MaxColors
Subject To
_C1: Noeud_('D',_0) + Noeud_('E',_0) <= 1
_C10: Noeud_('B',_3) + Noeud_('C',_3) <= 1
_C11: Noeud_('B',_4) + Noeud_('C',_4) <= 1
_C12: Noeud_('B',_5) + Noeud_('C',_5) <= 1
_C13: Noeud_('E',_0) + Noeud_('F',_0) <= 1
_C14: Noeud_('E',_1) + Noeud_('F',_1) <= 1
_C15: Noeud_('E',_2) + Noeud_('F',_2) <= 1
_C16: Noeud_('E',_3) + Noeud_('F',_3) <= 1
_C17: Noeud_('E',_4) + Noeud_('F',_4) <= 1
_C18: Noeud_('E',_5) + Noeud_('F',_5) <= 1
_C19: Noeud_('A',_0) + Noeud_('B',_0) <= 1
_C2: Noeud_('D',_1) + Noeud_('E',_1) <= 1
_C20: Noeud_('A',_1) + Noeud_('B',_1) <= 1
_C21: Noeud_('A',_2) + Noeud_('B',_2) <= 1
_C22: Noeud_('A',_3) + Noeud_('B',_3) <= 1
_C23: Noeud_('A',_4) + Noeud_('B',_4) <= 1
_C24: Noeud_('A',_5) + Noeud_('B',_5) <= 1
_C25: Noeud_('C',_0) + Noeud_('D',_0) <= 1
_C26: Noeud_('C',_1) + Noeud_('D',_1) <= 1
_C27: Noeud_('C',_2) + Noeud_('D',_2) <= 1
_C28: Noeud_('C',_3) + Noeud_('D',_3) <= 1
_C29: Noeud_('C',_4) + Noeud_('D',_4) <= 1
_C3: Noeud_('D',_2) + Noeud_('E',_2) <= 1
_C30: Noeud_('C',_5) + Noeud_('D',_5) <= 1
_C31: Noeud_('A',_0) + Noeud_('F',_0) <= 1
_C32: Noeud_('A',_1) + Noeud_('F',_1) <= 1
_C33: Noeud_('A',_2) + Noeud_('F',_2) <= 1
_C34: Noeud_('A',_3) + Noeud_('F',_3) <= 1
_C35: Noeud_('A',_4) + Noeud_('F',_4) <= 1
_C36: Noeud_('A',_5) + Noeud_('F',_5) <= 1
_C37: Noeud_('B',_0) + Noeud_('B',_1) + Noeud_('B',_2) + Noeud_('B',_3)
 + Noeud_('B',_4) + Noeud_('B',_5) = 1
_C38: Noeud_('A',_0) + Noeud_('A',_1) + Noeud_('A',_2) + Noeud_('A',_3)
 + Noeud_('A',_4) + Noeud_('A',_5) = 1
_C39: Noeud_('E',_0) + Noeud_('E',_1) + Noeud_('E',_2) + Noeud_('E',_3)
 + Noeud_('E',_4) + Noeud_('E',_5) = 1
_C4: Noeud_('D',_3) + Noeud_('E',_3) <= 1
_C40: Noeud_('F',_0) + Noeud_('F',_1) + Noeud_('F',_2) + Noeud_('F',_3)
 + Noeud_('F',_4) + Noeud_('F',_5) = 1
_C41: Noeud_('C',_0) + Noeud_('C',_1) + Noeud_('C',_2) + Noeud_('C',_3)
 + Noeud_('C',_4) + Noeud_('C',_5) = 1
_C42: Noeud_('D',_0) + Noeud_('D',_1) + Noeud_('D',_2) + Noeud_('D',_3)
 + Noeud_('D',_4) + Noeud_('D',_5) = 1
_C43: - MaxColors + Noeud_('A',_0) + Noeud_('A',_1) + Noeud_('A',_2)
 + Noeud_('A',_3) + Noeud_('A',_4) + Noeud_('A',_5) + Noeud_('B',_0)
 + Noeud_('B',_1) + Noeud_('B',_2) + Noeud_('B',_3) + Noeud_('B',_4)
 + Noeud_('B',_5) + Noeud_('C',_0) + Noeud_('C',_1) + Noeud_('C',_2)
 + Noeud_('C',_3) + Noeud_('C',_4) + Noeud_('C',_5) + Noeud_('D',_0)
 + Noeud_('D',_1) + Noeud_('D',_2) + Noeud_('D',_3) + Noeud_('D',_4)
 + Noeud_('D',_5) + Noeud_('E',_0) + Noeud_('E',_1) + Noeud_('E',_2)
 + Noeud_('E',_3) + Noeud_('E',_4) + Noeud_('E',_5) + Noeud_('F',_0)
 + Noeud_('F',_1) + Noeud_('F',_2) + Noeud_('F',_3) + Noeud_('F',_4)
 + Noeud_('F',_5) <= 0
_C5: Noeud_('D',_4) + Noeud_('E',_4) <= 1
_C6: Noeud_('D',_5) + Noeud_('E',_5) <= 1
_C7: Noeud_('B',_0) + Noeud_('C',_0) <= 1
_C8: Noeud_('B',_1) + Noeud_('C',_1) <= 1
_C9: Noeud_('B',_2) + Noeud_('C',_2) <= 1
Bounds
 1 <= MaxColors
Generals
MaxColors
Binaries
Noeud_('A',_0)
Noeud_('A',_1)
Noeud_('A',_2)
Noeud_('A',_3)
Noeud_('A',_4)
Noeud_('A',_5)
Noeud_('B',_0)
Noeud_('B',_1)
Noeud_('B',_2)
Noeud_('B',_3)
Noeud_('B',_4)
Noeud_('B',_5)
Noeud_('C',_0)
Noeud_('C',_1)
Noeud_('C',_2)
Noeud_('C',_3)
Noeud_('C',_4)
Noeud_('C',_5)
Noeud_('D',_0)
Noeud_('D',_1)
Noeud_('D',_2)
Noeud_('D',_3)
Noeud_('D',_4)
Noeud_('D',_5)
Noeud_('E',_0)
Noeud_('E',_1)
Noeud_('E',_2)
Noeud_('E',_3)
Noeud_('E',_4)
Noeud_('E',_5)
Noeud_('F',_0)
Noeud_('F',_1)
Noeud_('F',_2)
Noeud_('F',_3)
Noeud_('F',_4)
Noeud_('F',_5)
End
