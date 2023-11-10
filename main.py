from utility.BVA import BVA
from utility.BoundaryValueTableGenerator import BoundaryValueTableGenerator
from utility.EquationParser import EquationParser
from utility.InputHandler import InputHandler
import math

input_handler = InputHandler()
parser = EquationParser()
bva = BVA()

equation_str = input_handler.get_equation()

lhs_value, rhs_value, unique_symbols = parser.get_parsed_values(equation_str)

boundary_values = input_handler.get_boundary_values(unique_symbols)

boundary_value_table_generator = BoundaryValueTableGenerator()

boundary_value_table = boundary_value_table_generator.generate_table(unique_symbols, boundary_values)

boundary_value_table_generator.print_table(boundary_value_table)

test_cases = bva.get_all_combinations(boundary_value_table)
valid_test_cases, invalid_test_cases = bva.get_results(test_cases, boundary_value_table, lhs_value)

print('\n')
bva.print_test_cases("Valid", valid_test_cases)
print('\n')
bva.print_test_cases("Invalid", invalid_test_cases)
print('\n')

decision = input_handler.get_user_decision('Do you want to try a custom test case?')

while decision:
    case = []
    user_case = input_handler.get_user_case(unique_symbols)
    case.append(tuple(user_case))

    valid, invalid = bva.get_results(case, boundary_value_table, lhs_value)

    if valid:
        print(f"The case is Valid.")
        for case in valid:
            print("The output is: ", case["Output"])
    else:
        print(f"The case is Invalid.")
        for case in invalid:
            print("The error is: ", case["Output"])

    decision = input_handler.get_user_decision('Try another one?')
