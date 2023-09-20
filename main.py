
from itertools import permutations

symbols = ['+', '-', '*', '/']


def is_solved(nerdle: str) -> bool:
    parts = nerdle.split('=')
    sol = parts[-1]
    to_solve = parts[0]
    try:
        # print(f' | {to_solve} = {sol}', end=' ')
        # print(f' | {eval(to_solve)} = {eval(sol)}',end='')
        if eval(to_solve) == eval(sol):
            return True
        else:
            return False
    except SyntaxError:
        return False

def equal_is_last(nerdle: str) -> bool:
    return all(nerdle.index(symbol) < nerdle.index('=') 
               for symbol in symbols if symbol in nerdle)

def equal_is_first(nerdle: str) -> bool:
    return all(nerdle.index(symbol) > nerdle.index('=') 
               for symbol in symbols if symbol in nerdle)

def start_with_symbol(nerdle: str) -> bool:
    return any(nerdle.startswith(symbol) for symbol in symbols)

def two_symbols_adj(nerdle: str) -> bool:
    for symbol in symbols:
        if symbol in nerdle:
            pos = nerdle.index(symbol)
            if pos == 0:
                if is_symbol(nerdle[pos+1]):
                    return True
            elif pos == len(nerdle)-1:
                if is_symbol(nerdle[pos-1]):
                    return True
            else:
                if is_symbol(nerdle[pos-1]) or is_symbol(nerdle[pos+1]):
                    return True
    return False

def is_symbol(s: str) -> bool:
    return s in symbols



# *  4  7 [3] =  -  9  1
nerdle = input('Nerdle (for example: *473=-91):\n').replace(' ', '')
correct_pos = int(input('Correct green symbol (for example, the 3 in [*473=-91] is in position 4):\n')) - 1

fixed = nerdle[correct_pos]
perms = [''.join(p) for p in permutations(nerdle) if p[correct_pos] == fixed]

nerdle_str = []
for x in nerdle:
    if x == fixed:
        nerdle_str.append(f'[{x}]')
    else:
        nerdle_str.append(x)
nerdle_str = ' ' + ' '.join(nerdle_str) + ' '


print('=' * (len(nerdle_str) + 2))
print(f'|{nerdle_str}|')
print('=' * (len(nerdle_str) + 2))
print()

for nerdle in perms:
    """
    To be honest, I am not sure if the first condition (equal is last or equal is first)
    is necessary. Maybe the game accepts solution like X + Y = Z - T where = is in the 
    middle?.
    """

    if (equal_is_last(nerdle) or equal_is_first(nerdle)) \
        and not start_with_symbol(nerdle) \
        and not two_symbols_adj(nerdle):
        if is_solved(nerdle):
            nerdle_str = ' '.join([f"{x}" for x in nerdle])
            print(f'Solution: {nerdle_str} ✔️')
            break



