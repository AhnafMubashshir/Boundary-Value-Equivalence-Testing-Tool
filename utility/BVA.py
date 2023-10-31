import itertools


class BVA:
    @staticmethod
    def get_all_combinations(table):

        variable_details = []
        for entry in table:
            variable_value = []
            for key in entry.keys():
                if key != 'Symbol' and key != 'Min-' and key != 'Max+':
                    variable_value.append({'Symbol': entry['Symbol'], 'Value': entry[key]})

            variable_details.append(variable_value)

        all_combinations = list(itertools.product(*variable_details))

        return all_combinations

    @staticmethod
    def check_range(case, bva_table):
        for entry in bva_table:
            for variable in case:
                if variable['Symbol'] == entry['Symbol'] and (
                        variable['Value'] > entry['Max'] or variable['Value'] < entry['Min']):
                    return 'Invalid'

        return 'Passed'

    def get_results(self, cases, bva_table):
        test_case_with_result = []
        for case in cases:
            result = self.check_range(case, bva_table)
            test_case_with_result.append({'Output': result, 'Case': case})

        return test_case_with_result

    @staticmethod
    def print_test_cases(cases):
        print('Test cases:')
        for i, case in enumerate(cases, start=1):
            case_details = ''
            for variable in case['Case']:
                case_details = case_details + variable['Symbol'] + '=' + str(variable['Value']) + ' '
            print(f"Test-Case-id {i}: {case_details}, result: {case['Output']}")
