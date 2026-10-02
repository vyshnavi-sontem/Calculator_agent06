# Agentic AI - Agent Loop
# Key Concept: Observe -> Decide -> Act
# 3 Iterations

temperature = 80
goal = 72

for iteration in range(1, 4):

    # 1. OBSERVE
    print(f"\nIteration {iteration}")
    print("Observe: Temperature =", temperature)

    # 2. DECIDE
    if temperature > goal:
        decision = "Decrease temperature"
    elif temperature < goal:
        decision = "Increase temperature"
    else:
        decision = "Goal reached"

    print("Decide:", decision)

    # 3. ACT
    if decision == "Decrease temperature":
        temperature -= 1
    elif decision == "Increase temperature":
        temperature += 1

    print("Act: Temperature changed to", temperature)