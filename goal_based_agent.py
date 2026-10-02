# Goal-Driven Agentic AI
# Goal: Reach temperature = 72

temperature = 80
goal = 72

print("Initial temperature:", temperature)
print("Goal temperature:", goal)

while temperature != goal:

    # Agent decides an action based on the current state
    if temperature > goal:
        action = "Decrease temperature"
        temperature -= 1

    elif temperature < goal:
        action = "Increase temperature"
        temperature += 1

    print("Action:", action)
    print("Current temperature:", temperature)

print("\nGoal state reached!")
print("Temperature =", temperature)