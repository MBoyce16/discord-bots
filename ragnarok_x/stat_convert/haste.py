from utils import truncate_float

def haste_to_final_haste(haste:int) -> float:
    return round(0.2*((156.25 + (25*haste))**0.5), 2)

def haste_CD_reduc(haste: int) -> float:
    cd_reduc = 0.08 * ((156.25 + (25 * haste)) ** 0.5) - 1
    return truncate_float(cd_reduc, 1)

def fhaste_CD_reduc(final_haste: int) -> float:
    cd_reduc = (0.4 * final_haste) - 0.1
    return truncate_float(cd_reduc, 1)

def haste_CT_reduc(haste: int) -> float:
    ct_reduc = 0.005 * ((2500 + (400 * haste)) ** 0.5) - 0.25
    return truncate_float(ct_reduc, 1)

def fhaste_CT_reduc(final_haste: float) -> float:
    ct_reduc = (0.1 * final_haste) - 0.1
    return truncate_float(ct_reduc, 1)

def CD_reduc(haste: int, fhaste: float) -> float:
    cd_reduc = haste_CD_reduc(haste) + fhaste_CD_reduc(fhaste)
    return cd_reduc

def CT_reduc(haste: int, fhaste: float) -> float:
    ct_reduc = haste_CT_reduc(haste) + fhaste_CT_reduc(fhaste)
    return ct_reduc