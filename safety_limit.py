# Agentic AI - Agent Loop with Safety Limit
# Key Concept: max_iters prevents infinite loops

def temperature_agent(temperature, goal, max_iters=10):

    for iteration in range(1, max_iters + 1):

        # 1. OBSERVE
        print(f"\nIteration {iteration}")
        print("Observe: Temperature =", temperature)

        # Check goal
        if temperature == goal:
            print("Goal reached!")
            return "success"

        # 2. DECIDE
        if temperature > goal:
            action = "decrease"
        else:
            action = "increase"

        print("Decide:", action)

        # 3. ACT
        if action == "decrease":
            temperature -= 1
        else:
            temperature += 1

        print("Act: Temperature =", temperature)

    # Safety limit exceeded
    print("\nMaximum iterations exceeded.")
    return "failure"


# Run the agent
result = temperature_agent(
    temperature=80,
    goal=72,
    max_iters=10
)

print("\nResult:", result)

