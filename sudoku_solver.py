# This program is nothing special; I am simply coding along instead of 
# blindly following the python on the Udacity web page.
# I am doing this because I'm reviving my very rusty Python knowledge

# Unsolved boxes are denoted with a dot
# Binary representation of sudoku is as follows:
unsolved_puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
solved_puzzle = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'

# grid reference system will be 'A1', 'A2', ..... 'I9'
# Rows are letters, columns are numbers

# static definition of grid parameters. They're strings that will be parsed per character
rows = 'ABCDEFGHI'
cols = '123456789'

# helper function, concatenates to characters for unit display purposes
def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

"""
    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
     'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
     'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
     'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
     'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
     'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
     'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
     'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
     'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
"""

# define the sudoku row unit (A1, A2, A3 ...A9)
row_units = [cross(r, cols) for r in rows]

"""
[
['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], 
['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], 
['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], 
['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], 
['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], 
['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], 
['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], 
['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], 
['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
]
"""

# define sudoku column unit (A1, B1, C1, ... I1)
column_units = [cross(rows, c) for c in cols]

"""
[
['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], 
['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], 
['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], 
['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], 
['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], 
['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], 
['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], 
['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], 
['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9']   
]
"""

# Have to focus on this one, but this pulls box units (A1, A2, A3, B1, B2, B3, C1, C2, C3)
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

"""
[
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'], 
['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6'], 
['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9'], 
['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3'], 
['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'], 
['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9'], 
['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3'], 
['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6'], 
['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']
]
"""

# now we combine all three arangements into a unit list
unitlist = row_units + column_units + square_units

"""
[
    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], 
    ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], 
    ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], 
    ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], 
    ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'], 
    ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], 
    ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], 
    ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'], 
    ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], 
    
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], 
    ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], 
    ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'], 
    ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'], 
    ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'], 
    ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'], 
    ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'], 
    ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'], 
    ['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9'], 
    
    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'], 
    ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6'], 
    ['A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9'], 
    ['D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3'], 
    ['D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6'], 
    ['D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9'], 
    ['G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3'], 
    ['G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6'], 
    ['G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']
]
"""

# define a dictionary of units
# The dictionary structure is:
# {
# Each individual square(A1): list of the three types of units
# }
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
# see text file for print

# define a peers dictionary of all units that have relevance
# the print will be all over the place, but this is a nested dictionary of the 
# row, column, and square units that have logical significance
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

# I'm not great at this, but this is the helper display function to print the
# sudoku into an aesthetically pleasing console output
# This only has a pretty print when it has singlt dots
def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# The idea is to place all numbers (123456789) in the value is it's unassigned
def grid_values(grid):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(grid) == 81
    return dict(zip(boxes, values))

def eliminate(values):
    # We'll operate on a copy named solved_values
    # if a box is length one, it is a provided answer. Add it to list of solved values
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    # print(solved_values) # debugging
    for box in solved_values:     # now we iterate over every box that is a solved value
        digit = values[box]       # temp var for iterating across dict keys 
        # print('-----------------')
        # print('known answer:' + digit) # debugging
        for peer in peers[box]: 
            # print(box + ' : ' + values[peer]) # debugging 
            values[peer] = values[peer].replace(digit,'')
            # print(values[peer])  #debugging
            # print('-------------------') #debugging
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            poss_digits = [box for box in unit if digit in values[box]]
            if len(poss_digits) == 1:
                values[poss_digits[0]] = digit
    return values



# print(unsolved_puzzle)
# print()
puzzle = grid_values(unsolved_puzzle)
# print()
display(puzzle)
print()
# print(puzzle)
# print()
puzzle = eliminate(puzzle)
display(puzzle)
print()

puzzle = only_choice(puzzle)
display(puzzle)
print()

puzzle = eliminate(puzzle)
display(puzzle)
print()

puzzle = only_choice(puzzle)
display(puzzle)
print()

