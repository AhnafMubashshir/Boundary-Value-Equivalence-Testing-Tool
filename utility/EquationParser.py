from sympy import symbols, simplify, srepr
import re


class EquationParser:
    def __init__(self):
        self.lhs = symbols('lhs')
        self.rhs = symbols('rhs')

    @staticmethod
    def parse_equation(equation_str):
        lhs_str, rhs_str = equation_str.split('=')

        lhs_expr = simplify(lhs_str)
        rhs_expr = simplify(rhs_str)

        return lhs_expr, rhs_expr

    @staticmethod
    def get_unique_symbols(lhs_value):
        lhs_repr = srepr(lhs_value)

        unique_symbols = re.findall(r"Symbol\('(\w+)'\)", lhs_repr)

        return unique_symbols

    def get_parsed_values(self, equation_str):
        lhs_value, rhs_value = self.parse_equation(equation_str)
        unique_symbols = self.get_unique_symbols(lhs_value)
        return lhs_value, rhs_value, unique_symbols
