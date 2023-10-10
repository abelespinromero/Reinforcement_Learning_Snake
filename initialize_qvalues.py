
import json

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

if __name__ == "__main__":
    initialize_q_values()
