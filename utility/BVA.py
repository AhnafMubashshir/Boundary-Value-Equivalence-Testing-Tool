import itertools
import math
import re


class BVA:
    def validate_log(self, x):
        if x <= 0:
            raise ValueError("Logarithm value must be greater than 0. ")

    def validate_tan(self, x):
        if round(math.degrees(x)) % (360) == 90 or round(math.degrees(x)) % (360) == 270:
            raise ValueError("Tangent value cannot be the result of multiplying 90 degree by an odd number. ")

    def validate_cot(self, x):
        if round(math.degrees(x)) % (180) == 0:
            raise ValueError("Cotangent value cannot be an integer multiple of 180 degree. ")

    def validate_sec(self, x):
        if round(math.degrees(x)) % (360) == 90 or round(math.degrees(x)) % (360) == 270:
            raise ValueError("Secant value cannot be the result of multiplying 90 degree by an odd number. ")

    def validate_cosec(self, x):
        if round(math.degrees(x)) % (180) == 0:
            raise ValueError("Cosecant value cannot be an integer multiple of 180 degree. ")

    @staticmethod
    def get_all_combinations(table):

        variable_details = []
        for entry in table:
            variable_value = []
            for key in entry.keys():
                # if key != 'Symbol' and key != 'Min-' and key != 'Max+':
                if key != 'Symbol':
                    variable_value.append(
                        {'Symbol': entry['Symbol'], 'Value': entry[key]})

            variable_details.append(variable_value)

        all_combinations = list(itertools.product(*variable_details))

        return all_combinations

    @staticmethod
    def check_range(case, bva_table):
        for entry in bva_table:
            for variable in case:
                if variable['Symbol'] == entry['Symbol'] and (
                        variable['Value'] > entry['Max'] or variable['Value'] < entry['Min']):
                    return False

        return True
    
    def validate_variable_values(self, variable, equation):
        error = ''
        log_match = re.findall(r'log\((.*?)\)', equation)
        tan_match = re.findall(r'tan\((.*?)\)', equation)
        cot_match = re.findall(r"1/math.tan\((.*?)\)", equation)
        cosec_match = re.findall(r"1/math.sin\((.*?)\)", equation)
        sec_match = re.findall(r"1/math.cos\((.*?)\)", equation)

        if log_match:
            for var in log_match:
                if variable["Symbol"] == var:
                    try:
                        self.validate_log(variable['Value'])
                    except ValueError as ve:
                        error += str(ve)

        if tan_match:
            for var in tan_match:
                if variable["Symbol"] == var:
                    try:
                        self.validate_tan(variable['Value'])
                    except ValueError as ve:
                        error += str(ve)

        if cot_match:
            for var in cot_match:
                if variable["Symbol"] == var:
                    try:
                        self.validate_cot(variable['Value'])
                    except ValueError as ve:
                        error += str(ve)

        if cosec_match:
            for var in cosec_match:
                if variable["Symbol"] == var:
                    try:
                        self.validate_cosec(variable['Value'])
                    except ValueError as ve:
                        error += str(ve)

        if sec_match:
            for var in sec_match:
                if variable["Symbol"] == var:
                    try:
                        self.validate_sec(variable['Value'])
                    except ValueError as ve:
                        error += str(ve)

        return error
    
    def replace_trig_functions(self, match):
        function = match.group(1)
        return f"math.{function}("

    def get_outuput(self, case, equation):
        result = ''
        equation = str(equation)
        pattern = r'\b(tan|sin|cos|log)\s*\('
        equation = re.sub(pattern, self.replace_trig_functions, equation)

        values = {"math": math}
        for variable in case:
            result += self.validate_variable_values(variable, equation)
            globals()[variable['Symbol']] = variable["Value"]
            values[variable['Symbol']] = variable["Value"]

        if result == '':
            try:
                result = eval(equation, values)
                if math.isinf(result) or math.isnan(result):
                    raise ValueError("Math domain error")
                return str(result), True
            except (ValueError, ZeroDivisionError):
                return "Value Error", False
        else:
            return result, False

    def get_results(self, cases, bva_table, equation_str):
        valid_test_case_result = []
        invalid_test_case_result = []
        for case in cases:
            result = self.check_range(case, bva_table)
            if result == True:
                output, valid = self.get_outuput(case, equation_str)
                if valid: 
                    valid_test_case_result.append({'Output': output, 'Case': case})
                else:
                    invalid_test_case_result.append({'Output': output, 'Case': case})
            else:
                invalid_test_case_result.append(
                    {'Output': 'Invalid', 'Case': case})

        return valid_test_case_result, invalid_test_case_result

    @staticmethod
    def print_test_cases(case_name, cases):
        tan_symbol = "tan"
        cot_symbol = "cot"
        sin_symbol = "sin"
        cos_symbol = "cos"
        sec_symbol = "sec"
        cosec_symbol = "cosec"

        print(case_name, ' cases:')
        for i, case in enumerate(cases, start=1):
            case_details = ''
            for variable in case['Case']:
                if (tan_symbol or cot_symbol or sin_symbol or cos_symbol or sec_symbol or cosec_symbol) in variable['Symbol']:
                    case_details = case_details + \
                        variable['Symbol'] + '=' + str(round(math.degrees(variable['Value']))) + ' '
                else:
                    case_details = case_details + \
                        variable['Symbol'] + '=' + str(variable['Value']) + ' '
            print(
                f"Test-Case-id {i}: {case_details}, result: {case['Output']}")
