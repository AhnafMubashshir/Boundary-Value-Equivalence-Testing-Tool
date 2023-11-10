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

        unique_symbols = list(set(unique_symbols))

        return unique_symbols
    
    def replace_trig_function(self, equation):
        replacements = {
            'cot': r' (1/tan(\1)) ',
            'cosec': r' (1/sin(\1)) ',
            'sec': r' (1/cos(\1)) ',
        }
        
        function_names = ["cot", "cosec", "sec"]

        for function_name in function_names:
            if function_name in replacements:
                pattern = fr'{function_name}\s*\(\s*(.*?)\s*\)'
                equation = re.sub(pattern , replacements[function_name], equation)

        return equation
    
    def replace_tan_function_variables(self, match):
        variable = match.group(1)
        new_name = f"tan_{variable}"
        return f"tan({new_name})"
    
    def replace_sin_function_variables(self, match):
        variable = match.group(1)
        new_name = f"sin_{variable}"
        return f"sin({new_name})"
    
    def replace_cos_function_variables(self, match):
        variable = match.group(1)
        new_name = f"cos_{variable}"
        return f"cos({new_name})"
    
    def replace_cot_function_variables(self, match):
        variable = match.group(1)
        new_name = f"cot_{variable}"
        return f"cot({new_name})"
    
    def replace_cosec_function_variables(self, match):
        variable = match.group(1)
        new_name = f"cosec_{variable}"
        return f"cosec({new_name})"
    
    def replace_sec_function_variables(self, match):
        variable = match.group(1)
        new_name = f"sec_{variable}"
        return f"sec({new_name})"

    def get_parsed_values(self, equation_str):

        tan_pattern = r'tan\((.*?)\)'
        sin_pattern = r'sin\((.*?)\)'
        cos_pattern = r'cos\((.*?)\)'
        cot_pattern = r'cot\((.*?)\)'
        cosec_pattern = r'cosec\((.*?)\)'
        sec_pattern = r'sec\((.*?)\)'

        equation_str = re.sub(tan_pattern, self.replace_tan_function_variables, equation_str)
        equation_str = re.sub(sin_pattern, self.replace_sin_function_variables, equation_str)
        equation_str = re.sub(cos_pattern, self.replace_cos_function_variables, equation_str)
        equation_str = re.sub(cot_pattern, self.replace_cot_function_variables, equation_str)
        equation_str = re.sub(cosec_pattern, self.replace_cosec_function_variables, equation_str)
        equation_str = re.sub(sec_pattern, self.replace_sec_function_variables, equation_str)
        equation_str = self.replace_trig_function(str(equation_str))

        lhs_value, rhs_value = self.parse_equation(equation_str)
        unique_symbols = self.get_unique_symbols(lhs_value)
        return lhs_value, rhs_value, unique_symbols
