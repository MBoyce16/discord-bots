from collections import namedtuple
import typing as T
from stat_convert import total_crit, total_aspd, CD_reduc, CT_reduc
from dotenv.variables import Literal

"""
Need: 
@Target state: [crit, aspd, CD reduc, CT reduc]
@Target val: float
@current raw: int
@current final: float

@needed_stat: [raw, final]

1. Get formula based on target state
2. Calculate difference between target value and current target
3. Calculate difference between how much more stat is needed to target and current
4. Return how much more stat
"""

class NeededState:

    @staticmethod
    def clac_needed(stat:T.Literal['crit', 'aspd', 'CD reduction', 'CT reduction'],
                    needed_stat: T.Literal['raw', 'final'],
                    amount_stat_needed: float,
                    current_raw: int = 0,
                    current_final: float = 0):

        stat_calc = NeededState._get_calc(stat)
        current_val = stat_calc(current_raw, current_final)
        delta = amount_stat_needed - current_val





    @staticmethod
    def _get_calc(stat:T.Literal['crit', 'aspd', 'CD reduction', 'CT reduction']) -> callable:
        if stat == 'crit':
            calc = total_crit
        elif stat == 'aspd':
            calc = total_aspd
        elif stat == 'CD reduction':
            calc = CD_reduc
        elif stat == 'CT reduction':
            calc = CT_reduc

        return calc


