
import random
import json

class QLearner:
    def __init__(self):
        self.q_values = self.load_q_values()
        self.epsilon = 0.1 # Valor pequeño -> explotación, Valor grande -> exploración
        self.lr = 0.7 # Valor pequeño -> aprende lento, Valor grande -> aprende rapido (reacciona más rapido a las recompensas)
        self.discount_factor = .5 # Factor de descuento; Valor pequeño -> Priorizar recompensas/decisiones inmediatas,  Valor grande -> Priorizar recompensas/decisiones a largo plazo

    def load_q_values(self):
        try:
            with open("qvalues.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_q_values(self):
        with open("qvalues.json", "w") as f:
            json.dump(self.q_values, f)

    def state_to_str(self, snake, food, direction):
        return str((snake[0], food, direction))

    def select_action(self, snake, food, direction):
        state_str = self.state_to_str(snake, food, direction)

        # Epsilon greedy
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        else:
            action_values = self.q_values.get(state_str, {})
            if not action_values:
                return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
            return max(action_values, key=action_values.get)

    def update_q_values(self, old_snake, old_food, action, reward, new_snake, new_food, direction):
        old_state_str = self.state_to_str(old_snake, old_food, direction)
        new_state_str = self.state_to_str(new_snake, new_food, direction) if new_snake is not None else None

        old_q_value = self.q_values.get(old_state_str, {}).get(action, 0)
        max_new_q_value = 0 if new_state_str is None else max(self.q_values.get(new_state_str, {}).values(), default=0)

        new_q_value = (1 - self.lr) * old_q_value + self.lr * (reward + self.discount_factor * max_new_q_value)

        if old_state_str not in self.q_values:
            self.q_values[old_state_str] = {}
        self.q_values[old_state_str][action] = new_q_value
