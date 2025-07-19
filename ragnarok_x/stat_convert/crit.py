from math import floor


def crit_to_final_crit(crit:int) -> float:
   return round((6.25 + 2*crit)**0.5 - 2.5, 2)

def final_crit_to_crit(total_fcrit:float, fcrit:float=0) -> int:
   return int(((((total_fcrit - fcrit) + 2.5)**2) - 6.5)/2)

def total_crit(crit: int, fcrit: float) -> float:
   return fcrit + crit_to_final_crit(crit)