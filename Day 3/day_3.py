def is_symbol(c):
    symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
    return c in symbols

# given a valid location in the schematic, return the full part number
# if it exists at that location, otherwise None
# removes number from schematic if found
def is_part_number(loc, schematic):
    (col, row) = loc
    if(not schematic[row][col].isnumeric()):
        return None
    #print('loc:', loc, ': "', schematic[row][col], '"')
    n = int(schematic[row][col])
    start_num_idx = col
    end_num_idx = col

    # look right
    for i in range(len(schematic[row][col:])):
        if(not schematic[row][col+i].isnumeric()):
            break
        end_num_idx += 1
        #print('end idx:', end_num_idx)

    # look left
    for i in range(len(schematic[row][:col])):
        if(schematic[row][start_num_idx - 1].isnumeric()):
            start_num_idx -= 1
        else:
            break

    n = int(''.join(schematic[row][start_num_idx:end_num_idx]))
   # print('Before:', schematic[row])
    for i in range(start_num_idx, end_num_idx):
        schematic[row][i] = '.'
   # print('After: ', schematic[row])
   # print('num:', n)
    return n

with open('day_3_input.txt', 'r') as f:
    schematic = []
    symbol_loc = [] # location of all symbols
    for y, line in enumerate(f):
        l = []
        for i in range(len(line)):
            c = line[i]
            l.append(c)
            if(is_symbol(c)):
                symbol_loc.append((i,y)) # append location of each symbol

        schematic.append(l)

    #print(schematic)

    for c in ['*', 'j', '1', '.', '+', '-', '/', '"']:
        print(c, ':', is_symbol(c))
    print('symbol loc:', symbol_loc)
    part_numbers = []
    for (i, row) in symbol_loc:
        # look at all adjacent spaces, if a part number is there, add to list
        offset = [-1, 0, 1]
        for offset_row in offset:
            for offset_col in offset:
                if((offset_col, offset_row) == (0, 0)): # don't check self
                        continue
                r = row + offset_row
                c = i + offset_col
                if(r == -1 or r >= len(schematic)):
                    continue
                if(c == -1 or c >= len(schematic[0])):
                    continue
                pn = is_part_number((c, r), schematic)
                if(pn is not None):
                    part_numbers.append(pn)
                    
    print('\n', part_numbers)
    print('Sum:', sum(part_numbers))
