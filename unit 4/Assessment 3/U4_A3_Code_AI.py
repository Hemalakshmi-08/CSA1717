# ============================================================
# ANNEXURE A – INTEGRATED EXPERIMENTS
# Experiment 1: Decision Tree Classification (Iris Dataset)
# Experiment 2: Reinforcement Learning – Q-Learning (Grid World)
# ============================================================

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ============================================================
# EXPERIMENT 1: DECISION TREE CLASSIFICATION
# ============================================================

print("\n==============================")
print("EXPERIMENT 1: DECISION TREE")
print("==============================")

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display first 5 rows and data types
print("\nFirst 5 rows of dataset:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Split dataset
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Build Decision Tree using Gini Index
model = DecisionTreeClassifier(criterion='gini', random_state=42)
model.fit(X_train, y_train)

# Print tree structure
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nDecision Tree Structure:")
print(tree_rules)

# Identify root node
print("\nRoot Node (Feature with first split):")
root_node = tree_rules.split("\n")[0]
print(root_node)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Misclassified instances
misclassified = X_test[y_test != y_pred]
print("\nMisclassified Instances:")
print(misclassified)


# ============================================================
# EXPERIMENT 2: REINFORCEMENT LEARNING – Q-LEARNING
# ============================================================

print("\n==============================")
print("EXPERIMENT 2: Q-LEARNING GRID WORLD")
print("==============================")

# Grid World (4x4)
n_states = 16
n_actions = 4  # Up, Down, Left, Right

goal_state = 15
obstacle_state = 5

# Q-table
Q = np.zeros((n_states, n_actions))

# Hyperparameters
alpha = 0.7
gamma = 0.9
epsilon = 0.2

def get_next_state(state, action):
    row = state // 4
    col = state % 4

    if action == 0 and row > 0: row -= 1      # Up
    elif action == 1 and row < 3: row += 1    # Down
    elif action == 2 and col > 0: col -= 1    # Left
    elif action == 3 and col < 3: col += 1    # Right

    return row * 4 + col

def get_reward(state):
    if state == goal_state: return 10
    elif state == obstacle_state: return -5
    else: return -1

episodes = 100
rewards_per_episode = []

for ep in range(episodes):
    state = 0
    total_reward = 0

    while state != goal_state:
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[state])

        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state
        total_reward += reward

    rewards_per_episode.append(total_reward)

    if ep in [0, 49, 99]:
        print(f"\nQ-values at Episode {ep+1}:")
        print("State 0:", Q[0])
        print("State 10:", Q[10])

# Final Policy
policy = np.argmax(Q, axis=1)
print("\nFinal Learned Policy (0=Up,1=Down,2=Left,3=Right):")
print(policy.reshape(4,4))

# Plot cumulative reward
plt.plot(rewards_per_episode)
plt.xlabel("Episode")
plt.ylabel("Cumulative Reward")
plt.title("Q-Learning Convergence")
plt.show()
