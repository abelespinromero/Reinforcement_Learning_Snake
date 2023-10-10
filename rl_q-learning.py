
import numpy as np
from snake import play_game
import matplotlib.pyplot as plt

# Initialize Q-table and parameters
num_distance_bins = 20
num_angle_bins = 20
action_space_size = 4  # Up, Down, Left, Right

# Initialize Q-table with zeros
q_table = np.random.uniform(0, 0.1, (num_distance_bins, num_angle_bins, action_space_size))

learning_rate = 0.1
discount_rate = 0.99
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.0005

# Inicializa una lista para almacenar las puntuaciones de cada episodio
episode_scores = []


# Function to discretize state space
def discretize_state(state):
    distance, angle = state
    distance_bin = int(np.floor(distance / 50))
    angle_bin = int(np.floor((angle + np.pi) / (2 * np.pi / num_angle_bins)))
    return min(distance_bin, num_distance_bins - 1), min(angle_bin, num_angle_bins - 1)

# Function to take an action
def take_action(state, action):
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    action_direction = directions[action]
    new_state, reward, done = play_game(q_learning=True, action=action_direction)
    if new_state is not None:
        new_state = discretize_state(new_state)
    return new_state, reward, done


# Q-Learning training loop
num_episodes = 10000
for episode in range(num_episodes):
    print(f'Running episode: {episode + 1}')
    
    episode_score = 0  # Inicializa la puntuación para este episodio

    state, _, _ = play_game(q_learning=True)
    state = discretize_state(state)
    done = False

    while not done:
        if np.random.rand() > exploration_rate:
            action = np.argmax(q_table[state])
        else:
            action = np.random.randint(0, action_space_size)

        new_state, reward, done = take_action(state, action)
        episode_score += reward  # Accumulate the reward to the episode score

        if new_state is not None:
            q_table[state][action] = (1 - learning_rate) * q_table[state][action] + learning_rate * (reward + discount_rate * np.max(q_table[new_state]))
            state = new_state

    episode_scores.append(episode_score)  # Store the total episode score

    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)


# Plotting the scores
plt.plot(episode_scores)
plt.ylabel('Episode Scores')
plt.xlabel('Episode')
plt.title('Score per Episode')
plt.show()