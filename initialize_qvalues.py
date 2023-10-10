
import json

def initialize_q_values():
    q_values = {}
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    for x in range(0, 801, 10):
        for y in range(0, 601, 10):
            state = ((x, y),)
            q_values[str(state)] = {action: 0 for action in actions}

    with open("qvalues.json", "w") as f:
        json.dump(q_values, f)

if __name__ == "__main__":
    initialize_q_values()
