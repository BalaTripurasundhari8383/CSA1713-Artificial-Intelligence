def vacuum_cleaner(environment, location):
    steps = []

    while environment['A'] == 'dirty' or environment['B'] == 'dirty':
        steps.append((location, dict(environment)))  # Log the step

        if environment[location] == 'dirty':
            steps.append(f"Cleaning {location}")
            environment[location] = 'clean'
        else:
            if location == 'A':
                steps.append("Moving Right to B")
                location = 'B'
            else:
                steps.append("Moving Left to A")
                location = 'A'

    steps.append((location, dict(environment)))
    steps.append("All rooms are clean!")

    return steps

# Example environment setup
initial_env = {
    'A': 'dirty',
    'B': 'dirty'
}
initial_location = 'A'

result = vacuum_cleaner(dict(initial_env), initial_location)

# Print the steps
print("Vacuum Cleaner Simulation:")
for step in result:
    print(step)
