
from snake_game import GameLoop
import q_learner
from constants import TEXT_COLOR, SNAKE_COLOR , FOOD_COLOR, BACKGROUND_COLOR, BLOCK_SIZE, DIS_WIDTH, DIS_HEIGHT, QVALUES_N, FRAMESPEED
import matplotlib.pyplot as plt



def main():

    learner = q_learner.Q_Learner(DIS_WIDTH, DIS_HEIGHT, BLOCK_SIZE)
    scores = []
    
    n_episodes = 300
    for episode in range(0, n_episodes):
        
        learner.Reset()
        if episode > 100:
            learner.epsilon = 0
        else:
            learner.epsilon = .1
        score, reason = GameLoop(learner)
        scores.append(score)

        print(f"Games: {episode}; Score: {score}; Reason: {reason}") # Output results of each game to console to monitor as agent is training

        if episode % QVALUES_N == 0: # Save qvalues every qvalue_dump_n games
            print("Save Qvals")
            learner.SaveQvalues()

    plt.plot(range(0, n_episodes), scores)
    plt.xlabel("Episode")
    plt.ylabel("Score")
    plt.show()

if __name__ == "__main__":
    main()