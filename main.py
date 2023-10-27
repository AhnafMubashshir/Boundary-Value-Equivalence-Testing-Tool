from utility.BoundaryValueTableGenerator import BoundaryValueTableGenerator
from utility.EquationParser import EquationParser
from utility.InputHandler import InputHandler

input_handler = InputHandler()
parser = EquationParser()

equation_str = input_handler.get_equation()

lhs_value, rhs_value, unique_symbols = parser.get_parsed_values(equation_str)

boundary_values = input_handler.get_boundary_values(unique_symbols)

boundary_value_table_generator = BoundaryValueTableGenerator()

boundary_value_table = boundary_value_table_generator.generate_table(unique_symbols, boundary_values)

print("Boundary Value Table:")
for entry in boundary_value_table:
    print(entry)
