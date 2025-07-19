

def aspd_to_final_aspd(aspd:int) -> float:
    return round(50*((0.25 + 0.04*aspd)**0.5) - 25, 2)

def final_aspd_to_aspd(total_faspd:float, faspd:float=0) -> int:
    return int((((((total_faspd - faspd) + 25)/50)**2) - 0.025)/0.04)

def total_aspd(aspd:int, faspd:float) -> float:
    return faspd + aspd_to_final_aspd(aspd)