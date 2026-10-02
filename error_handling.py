# Agentic AI - Error Handling
# Key Concept: Handle invalid action and return error dict

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

        elif temperature < goal:
            action = "increase"

        else:
            action = "invalid"

        # 3. HANDLE ACTION
        if action == "decrease":
            temperature -= 1

        elif action == "increase":
            temperature += 1

        elif action == "goal_reached":
            state["done"] = True

        else:
            # Invalid action → return error
            return {
                "status": "error",
                "error": "Invalid action",
                "action": action,
                "step": state["steps"] + 1,
                "temperature": temperature,
                "log": log
            }

        # Track step
        state["steps"] += 1

        # Log the step
        log.append({
            "step": state["steps"],
            "observed_temperature": old_temperature,
            "action": action,
            "new_temperature": temperature,
            "done": state["done"]
        })

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

print("Result:")
print(result)