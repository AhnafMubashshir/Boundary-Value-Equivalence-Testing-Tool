import math
import re

class InputHandler:
    @staticmethod
    def get_boundary_values(unique_symbols):
        boundary_values = {}
        for symbol in unique_symbols:
            print('\n')
            if re.search(r'(tan|cos|sin)', symbol):
                low = float(input(f"Enter the low boundary value in degrees for symbol '{symbol}': "))
                high = float(input(f"Enter the high boundary value in degrees for symbol '{symbol}': "))
                boundary_values[symbol] = {'low': math.radians(low), 'high': math.radians(high)}
            else:
                low = float(input(f"Enter the low boundary value for symbol '{symbol}': "))
                high = float(input(f"Enter the high boundary value for symbol '{symbol}': "))
                boundary_values[symbol] = {'low': low, 'high': high}

        return boundary_values

    @staticmethod
    def get_equation():
        return input("Enter an equation (e.g., '4*x + x*x + tan(x) + log(10) + 1 = 13'): ")

    def get_user_case(self, unique_symbols):
        user_case = []
        for symbol in unique_symbols:
            if re.search(r'(tan|cos|sin)', symbol):
                symbol_value = float(input(f"Enter value in degrees for symbol '{symbol}': "))
                user_case.append({'Symbol': symbol, 'Value': math.radians(symbol_value)})
            else:
                symbol_value = float(input(f"Enter value for symbol '{symbol}': "))
                user_case.append({'Symbol': symbol, 'Value': symbol_value})
        return user_case

    def get_user_decision(self, message):
        user_input = input(f"{message} (Y/n): ")

        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        else:
            return "Invalid input. Please enter 'y' or 'n'."

