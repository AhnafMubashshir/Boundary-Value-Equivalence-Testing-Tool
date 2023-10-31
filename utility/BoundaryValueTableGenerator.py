class BoundaryValueTableGenerator:
    @staticmethod
    def generate_table(unique_symbols, boundary_values):
        table = []
        for symbol in unique_symbols:
            low = boundary_values[symbol]['low']
            high = boundary_values[symbol]['high']
            nominal = int((low + high) / 2)
            min_plus = low + 1
            max_minus = high - 1
            max_plus = high + 1
            min_minus = low - 1

            table.append({
                'Symbol': symbol,
                'Min': low,
                'Max': high,
                'Min+': min_plus,
                'Max-': max_minus,
                'Max+': max_plus,
                'Min-': min_minus,
                'Nominal': nominal
            })

        return table

    @staticmethod
    def print_table(table):
        print("Boundary Value Table:")
        for entry in table:
            print(entry)
