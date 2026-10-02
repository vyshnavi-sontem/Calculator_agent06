# Agentic AI - Observability
# Key Concept: Log each step and return full log

def temperature_agent(temperature, goal, max_iters=10):

    state = {
        "done": False,
        "steps": 0
    }

    # Store every step
    log = []

    while not state["done"] and state["steps"] < max_iters:

        # 1. OBSERVE
        old_temperature = temperature

        # 2. DECIDE
        if temperature == goal:
            state["done"] = True
            action = "goal reached"

        elif temperature > goal:
            action = "decrease"
            temperature -= 1

        else:
            action = "increase"
            temperature += 1

        # Track step
        state["steps"] += 1

        # 3. LOG THE STEP
        log.append({
            "step": state["steps"],
            "observed_temperature": old_temperature,
            "action": action,
            "new_temperature": temperature,
            "done": state["done"]
        })

    # Determine final status
    if temperature == goal:
        status = "success"
        state["done"] = True
    else:
        status = "failure"

    # Return complete information
    return {
        "status": status,
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

print("Status:", result["status"])
print("Steps:", result["steps"])
print("Final Temperature:", result["final_temperature"])

print("\nFull Log:")
for entry in result["log"]:
    print(entry)