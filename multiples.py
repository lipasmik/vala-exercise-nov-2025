import os
import argparse

class MultiplesHandler:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file


    def validate_input(self) -> None:
        '''
        Validates the input file for various conditions, like empty or non-existing file,
        correct amount of numbers per line, and natural number checks.
        '''
        input_file = self.input_file
        output_file = self.output_file
        if input_file == output_file:
            raise ValueError("Input and output file names must be different.")
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file {input_file} does not exist.")
        if os.path.getsize(input_file) == 0:
            raise ValueError("Input file is empty.")
        try:
            with open(input_file, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    line = line.replace('\n', '')
                    if len(line) == 0:
                        raise ValueError(f"{input_file}: {line_number}: line is empty.")
                    if line[0] == ' ' or line[-1] == ' ':
                        raise ValueError(f"{input_file}: {line_number}: line contains leading or trailing spaces")
                    numbers_in_line = line.strip().split()
                    if len(numbers_in_line) != 3:
                        raise ValueError(f"{input_file}: {line_number}: each line must contain exactly three numbers.")
                    for number in numbers_in_line:
                        if not number.isdigit():
                            raise TypeError(f"{input_file}: {line_number}: line contains non natural values.")
                        if int(number) < 1:
                            raise ValueError(f"{input_file}: {line_number}: line contains values < 1.")
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"{input_file} contains non unicode characters.")
        except PermissionError:
            raise PermissionError(f"Permission denied for file {input_file}.")


    def process_multiples(self)-> list[tuple]:
        '''
        Processes the input file to find multiples of two numbers up to a goal number.
        Returns a sorted list of tuples containing the goal number and its corresponding multiples.
        '''
        all_results = []
        with open(self.input_file, 'r') as file:
            for line in file:
                results = []
                line = line.replace('\n', '')
                num1, num2, goal_number = map(int, line.split(' '))
                for i in range(1, goal_number):
                    valid_multipliers = [i*number for number in [num1, num2] if i*number < goal_number]
                    results.extend(list(set(valid_multipliers)))
                    if i*num1 >= goal_number and i*num2 >= goal_number:
                        break
                results = list(set(results))
                results.sort()
                all_results.append((goal_number, results))
            all_results_sorted = sorted(all_results, key=lambda x: len(x[1]))
            return all_results_sorted


    def output_results(self, all_results_sorted: list)-> None:
        '''
        Outputs the results to the console and writes them to the output file.
        '''
        for item in all_results_sorted:
            print(f'{item[0]}:{" ".join(map(str, item[1]))}')
        with open(self.output_file, 'w') as file:
            for i, item in enumerate(all_results_sorted):
                line = f'{item[0]}:{" ".join(map(str, item[1]))}'
                if i != len(all_results_sorted) - 1:
                    line += '\n'
                file.write(line)



def parse_args():
    parser = argparse.ArgumentParser(description="Process multiples from input file and write to output file.")
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    multiples_handler = MultiplesHandler(args.input_file, args.output_file)
    multiples_handler.validate_input()
    results = multiples_handler.process_multiples()
    multiples_handler.output_results(results)
