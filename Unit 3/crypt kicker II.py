import sys
import string

ALPHABET = string.ascii_lowercase
ALPHABET_SET = set(ALPHABET)
PLAINTEXT = 'the quick brown fox jumps over the lazy dog'



def load_case():
    case = []
    
    for line in sys.stdin:
        if line =='\n':
            break
        else:
            case.append(line.rstrip())

    return case


def has_same_spaces(plain, encode):

    if len(plain) != len(encode):
        return False
    # count number of spaces 
    if plain.count(' ') != encode.count(' '):
        return False


    return True


def has_all_chars(encode):

    return set(encode.replace(' ', '')) == ALPHABET_SET


def substitute(line, subs):
    return "".join(subs[c] for c in line)


def decode(case):
    
    key = None

    # Search plaintext candidate line
    for line in case:
        # Spaces same place
        
        if not has_same_spaces(PLAINTEXT, line):
            continue

        # All characters have to be present in a key candidate
        if not has_all_chars(line):
            continue
       
        key = line
        break

    if key is None:
        return None

    # Create substitution table
    subs = {}
    for k, p in zip(key, PLAINTEXT):
        subs[k] = p

    # Decode all lines
    dec = []
    for line in case:
        dec.append(substitute(line, subs))

    return dec



cases = int(input())

sys.stdin.readline()
    
for i in range(cases): 
    dec = decode(load_case())
    if not dec:
        print('No solution.')
    else:
        for line in dec:
            print(line)
       
    if i+1<cases:
        print('')
