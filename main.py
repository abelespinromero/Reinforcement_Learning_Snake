
from snake_game import play_game
from q_learner import QLearner
import matplotlib.pyplot as plt

def main():
    q_learner = QLearner()
    scores = []
    
    n_episodes = 10000
    for episode in range(0, n_episodes):
        print(f"Episode: {episode}")
        score = play_game(q_learner=q_learner)
        scores.append(score)
        q_learner.save_q_values()
        
    plt.plot(range(0, n_episodes), scores)
    plt.xlabel("Episode")
    plt.ylabel("Score")
    plt.show()

if __name__ == "__main__":
    main()
