from idlelib.run import Executive

from sympy import symbols, Eq, solve
import typing as T

class Stat:
    def __init__(self):
        self.raw = symbols('raw', interger=True, positive=True)
        self.final = symbols('final', integer=False)
        self.stat = symbols('stat', integer=False, postive=True)

        self.raw_expr = self.raw
        self.final_expr = self.final

        self.base_eq = Eq(self.raw_expr + self.final_expr, self.stat)

    def _solve(self, inputs:T.Dict[str, T.Union[float, int]]):
        frmt_inputs = {self._get(k): v for k,v in inputs.items()}
        eq_to_solve = self.base_eq.subs(frmt_inputs)
        result = solve(eq_to_solve)[0]
        return result

    def _get(self, attr:str) -> T.Any:
        return self.__getattribute__(attr)

    def convert_input(self,
                      input_type: T.Literal['raw', 'final'],
                      input_val:T.Union[float, int]) -> str:

        needed_name = self._get(input_type + '_name')
        raw_val = input_val if input_type == 'raw' else 0
        final_val = input_val if input_type == 'final' else 0

        input_dict = {'raw': raw_val, 'final': final_val}
        result = self._solve(input_dict)

        return f'{input_val} {needed_name} provides {result:.2f} {self.name}'

    def compare_inputs(self,
                       raw:int,
                       final:float,
                       current_raw:int,
                       current_final:float) -> str:

        current_dict = {'raw': current_raw, 'final': current_final}
        raw_dict = {'raw': raw + current_raw, 'final': current_final}
        final_dict = {'raw': current_raw, 'final': final + current_final}

        current_solve = self._solve(current_dict)
        final_solve = self._solve(raw_dict)
        raw_solve = self._solve(final_dict)

        return f'Raw stat adds :{(raw_solve - current_solve):.0f} {self.name},\nFinal stat adds: {(final_solve - current_solve):.2f} {self.name}'

    def needed_input(self,
                    current_raw:int,
                    current_final: float,
                    stat_to_quant:T.Literal['raw', 'final'],
                    target_amt: float) -> str:

        needed_name = self._get(stat_to_quant + '_name')

        if stat_to_quant == 'raw':
            quant_val = current_raw
            static_val = current_final
            static_stat = 'final'

        elif stat_to_quant == 'final':
            quant_val = current_final
            static_val = current_raw
            static_stat = 'raw'

        else:
            raise Exception(f'Stat to quant {stat_to_quant} needs to be "raw" or "final"')


        input_dict = {static_stat: static_val, 'stat': target_amt}
        result = self._solve(input_dict)

        stat_needed = result - quant_val

        return f'To reach {target_amt} {self.name}, you need: {stat_needed:.2f} {needed_name}'
