# Agentic AI - 2 Step Loop
# Key Concept: Code Reading

temperature = 80
goal = 78

for step in range(2):

    print("Step:", step + 1)
    print("Observe:", temperature)

    if temperature > goal:
        action = "decrease"
        temperature -= 1
    else:
        action = "increase"
        temperature += 1

    print("Action:", action)
    print("Temperature:", temperature)