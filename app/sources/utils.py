import numpy as np

# Algorithm for generating match sequence
def generate_matches():
    matches = []
    for i in range(4):
        for j in range(3):
            if [i, j] not in matches and [j, i] not in matches and i != j:
                matches.append([i, j])
    return matches

# Algorithm for estimating match results
def estimate_results(team_a, team_b, penalties=False):
    std = 1.0
    prop_a = 1.25 + 0.15*(team_a[1] - team_b[0])
    prop_b = 1.25 + 0.15*(team_b[1] - team_a[0])
    if penalties:
        prop = 4
        a = int(np.random.normal(prop, std))
        b = int(np.random.normal(prop, std))
    else:
        a = int(np.random.normal(prop_a, std))
        b = int(np.random.normal(prop_b, std)) 
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    if penalties:
        if a > 4 and a > b:
            b = a - 1
        elif b > 4 and b > a:
            a = b - 1
        elif a - b > 3:
            b += (a-b) - 3
        elif b - a > 3:
            a += (b-a) - 3
    return [a, b]