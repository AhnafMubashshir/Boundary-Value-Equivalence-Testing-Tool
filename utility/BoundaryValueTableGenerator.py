import math


class BoundaryValueTableGenerator:
    @staticmethod
    def generate_table(unique_symbols, boundary_values):
        table = []
        for symbol in unique_symbols:
            tan_symbol = "tan"
            cot_symbol = "cot"
            sin_symbol = "sin"
            cos_symbol = "cos"
            sec_symbol = "sec"
            cosec_symbol = "cosec"

            low = boundary_values[symbol]['low']
            high = boundary_values[symbol]['high']
            max_plus = 0
            max_minus = 0
            min_plus = 0
            min_minus = 0

            if (tan_symbol or cot_symbol or sin_symbol or cos_symbol or sec_symbol or cosec_symbol) in symbol:
                min_plus = math.radians(round(math.degrees(low))+1)
                max_minus = math.radians(round(math.degrees(high))-1)
                max_plus = math.radians(round(math.degrees(high))+1)
                min_minus = math.radians(round(math.degrees(low))-1)
                nominal = math.radians(
                    (round(math.degrees(low)) + round(math.degrees(high))) / 2)
            else:
                min_plus = low + 1
                max_minus = high - 1
                max_plus = high + 1
                min_minus = low - 1
                nominal = (low + high) / 2

            table.append({
                'Symbol': symbol,
                'Min': low,
                'Max': high,
                'Min+': min_plus,
                'Max-': max_minus,
                'Max+': max_plus,
                'Min-': min_minus,
                'Nominal': nominal,
            })

        return table

    @staticmethod
    def print_table(table):
        print("Boundary Value Table:")
        for entry in table:
            print(entry)
