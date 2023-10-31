from utility.BVA import BVA
from utility.BoundaryValueTableGenerator import BoundaryValueTableGenerator
from utility.EquationParser import EquationParser
from utility.InputHandler import InputHandler

input_handler = InputHandler()
parser = EquationParser()
bva = BVA()

equation_str = input_handler.get_equation()

lhs_value, rhs_value, unique_symbols = parser.get_parsed_values(equation_str)

boundary_values = input_handler.get_boundary_values(unique_symbols)

boundary_value_table_generator = BoundaryValueTableGenerator()

boundary_value_table = boundary_value_table_generator.generate_table(unique_symbols, boundary_values)

# boundary_value_table_generator.print_table(boundary_value_table)

test_cases = bva.get_all_combinations(boundary_value_table)
test_cases = bva.get_results(test_cases, boundary_value_table)
bva.print_test_cases(test_cases)

decision = input_handler.get_user_decision('Do you want to try a custom test case?')

while decision:
    user_case = input_handler.get_user_case(unique_symbols)

    user_case_result = bva.check_range(user_case, boundary_value_table)

    print(f"The case is: {user_case_result}")

    decision = input_handler.get_user_decision('Try another one?')


