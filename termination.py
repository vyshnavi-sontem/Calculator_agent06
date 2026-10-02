# Agentic AI - Termination
# Key Concept: Success / Failure Status

def temperature_agent(temperature, goal, max_iters=10):

    state = {
        "done": False,
        "steps": 0
    }

    while not state["done"] and state["steps"] < max_iters:

        # 1. OBSERVE
        print(f"\nStep {state['steps'] + 1}")
        print("Observe: Temperature =", temperature)

        # 2. DECIDE
        if temperature == goal:
            state["done"] = True
            status = "success"

        elif temperature > goal:
            action = "decrease"
            temperature -= 1
            status = "running"

        else:
            action = "increase"
            temperature += 1
            status = "running"

        # Track steps
        state["steps"] += 1

        print("Act: Temperature =", temperature)
        print("Status:", status)

    # TERMINATION
    if temperature == goal:
        state["done"] = True
        return {
            "status": "success",
            "steps": state["steps"],
            "temperature": temperature
        }

    else:
        return {
            "status": "failure",
            "steps": state["steps"],
            "temperature": temperature
        }


# Run the agent
result = temperature_agent(
    temperature=80,
    goal=72,
    max_iters=10
)

print("\nFinal Result:")
print(result)