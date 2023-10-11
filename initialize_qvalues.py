
import json
import itertools

"""

width, height = 400, 300

def initialize_q_values():
    q_values = {}
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    for x in range(0, width+1, 10):
        for y in range(0, height+1, 10):
            state = ((x, y),)
            q_values[str(state)] = {action: 0 for action in actions}

    with open("qvalues.json", "w") as f:
        json.dump(q_values, f)
"""

def initialize_q_values():
    sqs = [''.join(s) for s in list(itertools.product(*[['0','1']] * 4))]
    widths = ['0','1','NA']
    heights = ['2','3','NA']

    states = {}
    for i in widths:
        for j in heights:
            for k in sqs:
                states[str((i,j,k))] = [0,0,0,0]

    with open("qvalues.json", "w") as f:
        json.dump(states, f)

if __name__ == "__main__":
    initialize_q_values()