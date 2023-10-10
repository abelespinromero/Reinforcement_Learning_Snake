
import numpy as np
from snake import play_game  # Make sure the updated snake.py is in the same directory or adjust the import

# Initialize Q-table and parameters
state_space_size = 800 * 600  # Considering each pixel as a state
action_space_size = 4  # Up, Down, Left, Right
q_table = np.zeros((state_space_size, action_space_size))
learning_rate = 0.1
discount_rate = 0.99
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

# Function to get state index
def get_state_index(state):
    x, y = state
    return x + 800 * y

# Function to get initial state and take an action
def get_initial_state():
    # Call play_game from snake.py to get the initial state
    initial_state, _, _ = play_game(q_learning=True, action="RIGHT")
    return get_state_index(initial_state)

def take_action(state, action):
    # Convert the action index to a direction
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    action_direction = directions[action]
    
    # Call play_game from snake.py to take an action and get the new state and reward
    new_state, reward, done = play_game(q_learning=True, action=action_direction)
    new_state_index = get_state_index(new_state)
    return new_state_index, reward, done

# Q-Learning training loop
num_episodes = 10000
for episode in range(num_episodes):
    print(f'Running episode: {episode + 1}')
    
    state = get_initial_state()
    done = False

    while not done:
        if np.random.rand() > exploration_rate:
            action = np.argmax(q_table[state, :])
        else:
            action = np.random.randint(0, action_space_size)

        new_state, reward, done = take_action(state, action)
        q_table[state, action] = (1 - learning_rate) * q_table[state, action] + learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
        state = new_state

    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)
