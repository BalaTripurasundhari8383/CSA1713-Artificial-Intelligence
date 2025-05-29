import itertools

def solve_cryptarithmetic():
    # Unique characters in SEND + MORE = MONEY
    letters = 'SENDMORY'
    assert len(letters) == 8  # should be 8 unique letters

    # All possible digit permutations for 8 unique letters
    for perm in itertools.permutations(range(10), 8):
        assign = dict(zip(letters, perm))

        # Skip if S or M is assigned to 0 (no leading zeros)
        if assign['S'] == 0 or assign['M'] == 0:
            continue

        # Construct numbers from letters
        send = 1000*assign['S'] + 100*assign['E'] + 10*assign['N'] + assign['D']
        more = 1000*assign['M'] + 100*assign['O'] + 10*assign['R'] + assign['E']
        money = 10000*assign['M'] + 1000*assign['O'] + 100*assign['N'] + 10*assign['E'] + assign['Y']

        if send + more == money:
            print("Solution found:")
            print(f"SEND:  {send}")
            print(f"MORE:  {more}")
            print(f"MONEY: {money}")
            print(f"Mapping: {assign}")
            return

    print("No solution found.")

solve_cryptarithmetic()
