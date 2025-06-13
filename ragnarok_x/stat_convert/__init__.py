from aspd import (aspd_to_final_aspd, total_aspd)
from crit import (crit_to_final_crit, total_crit)
from haste import (haste_to_final_haste, CD_reduc, CT_reduc)

import typing as T

def formula_factory(stat: T.Literal['crit', 'haste', 'aspd']) -> T.Union[callable, None]:
    val_stat = stat.lower().strip()
    if val_stat == 'crit':
        calc = crit_to_final_crit
    elif val_stat == 'aspd':
        calc = aspd_to_final_aspd
    elif val_stat == 'haste':
        calc = haste_to_final_haste
    else:
        calc = None
    return calc