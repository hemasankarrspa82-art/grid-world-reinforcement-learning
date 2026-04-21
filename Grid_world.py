
import numpy as np

grid = np.zeros((4, 4))
goal = (3, 3)

def move(state, action):
    x, y = state
    if action == "up":
        x = max(0, x-1)
    elif action == "down":
        x = min(3, x+1)
    elif action == "left":
        y = max(0, y-1)
    elif action == "right":
        y = min(3, y+1)
    return (x, y)

state = (0, 0)
steps = 0

while state != goal:
    action = np.random.choice(["up", "down", "left", "right"])
    state = move(state, action)
    steps += 1
    print("Moved to:", state)

print("Reached Goal in", steps, "steps")
