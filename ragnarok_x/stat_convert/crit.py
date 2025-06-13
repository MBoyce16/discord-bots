

def crit_to_final_crit(crit:int) -> float:
   return round((6.25 + 2*crit)**0.5 - 2.5, 2)

def total_crit(crit: int, fcrit: float) -> float:
   return fcrit + crit_to_final_crit(crit)