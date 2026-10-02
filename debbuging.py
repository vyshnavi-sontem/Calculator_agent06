# Agentic AI - Debugging
# Key Concept: Find and fix missing loop increment

def temperature_agent(temperature, goal, max_iters=10):

    state = {
        "done": False,
        "steps": 0
    }

    log = []

    while not state["done"] and state["steps"] < max_iters:

        # 1. OBSERVE
        old_temperature = temperature

        # 2. DECIDE
        if temperature == goal:
            action = "goal_reached"

        elif temperature > goal:
            action = "decrease"

        else:
            action = "increase"

        # 3. ACT
        if action == "decrease":
            temperature -= 1

        elif action == "increase":
            temperature += 1

        elif action == "goal_reached":
            state["done"] = True

        # BUG FIX:
        # The loop must increment the step counter.
        state["steps"] += 1

        # Log the step
        log.append({
            "step": state["steps"],
            "observed_temperature": old_temperature,
            "action": action,
            "new_temperature": temperature,
            "done": state["done"]
        })

        print(
            f"Step {state['steps']}: "
            f"{old_temperature} -> {temperature}, "
            f"Action: {action}"
        )

    # Termination
    if temperature == goal:
        return {
            "status": "success",
            "steps": state["steps"],
            "final_temperature": temperature,
            "log": log
        }

    return {
        "status": "failure",
        "error": "Maximum iterations exceeded",
        "steps": state["steps"],
        "final_temperature": temperature,
        "log": log
    }


# Run the agent
result = temperature_agent(
    temperature=80,
    goal=72,
    max_iters=10
)

print("\nFinal Result:")
print(result)