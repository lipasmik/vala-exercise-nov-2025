# README

## VALA coding exercise: Multiplies (by Mikko Lipasti)

### To run the program:

Prerequisite: install python (if not installed)

Place input file in the same folder `multiples.py` is located.

Running the program: `python multiples.py <input_file> <output_file>`, e.g. `python multiples.py input.txt output.txt`

### Improvement suggestions:
- Memory handling in method process_multiples could be improved in order to handle situations where user inputs really small numbers to be multiplied (e.g. 1, 2) and a really large goal number (e.g. 1,000,000)
- Unit tests (e.g. `pytest`) could be added