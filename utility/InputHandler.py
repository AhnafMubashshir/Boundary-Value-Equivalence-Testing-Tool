class InputHandler:
    def get_boundary_values(self, unique_symbols):
        boundary_values = {}
        for symbol in unique_symbols:
            low = float(input(f"Enter the low boundary value for symbol '{symbol}': "))
            high = float(input(f"Enter the high boundary value for symbol '{symbol}': "))
            boundary_values[symbol] = {'low': low, 'high': high}
        return boundary_values

    def get_equation(self):
        return input("Enter an equation (e.g., '4*n + x - y = 13'): ")

